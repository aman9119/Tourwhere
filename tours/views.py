from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from .models import Destination, Tour, Booking, Profile
from .forms import BookingForm, ProfileForm, ReviewForm

def home(request):
    featured_tours = Tour.objects.all()[:3]  # Show 3 featured tours (customize as needed)
    return render(request, 'tours/home.html', {'featured_tours': featured_tours})

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'tours/destination_list.html', {'destinations': destinations})

def tour_list(request):
    query = request.GET.get('q', '')
    destination_id = request.GET.get('destination', '')
    tours = Tour.objects.all()
    destinations = Destination.objects.all()
    if query:
        tours = tours.filter(title__icontains=query)
    if destination_id:
        tours = tours.filter(destination_id=destination_id)
    return render(request, 'tours/tour_list.html', {
        'tours': tours,
        'destinations': destinations,
        'query': query,
        'selected_destination': destination_id
    })

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    reviews = tour.reviews.select_related('user').order_by('-created_at')
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
    review_form = None
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
        if not user_review:
            review_form = ReviewForm()
    if request.method == 'POST' and request.user.is_authenticated and not user_review:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.tour = tour
            review.user = request.user
            review.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'rating': review.rating, 'comment': review.comment, 'username': request.user.username})
            return redirect('tour_detail', tour_id=tour.id)
        elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': review_form.errors}, status=400)
    return render(request, 'tours/tour_detail.html', {
        'tour': tour,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'review_form': review_form,
        'user_review': user_review
    })

def book_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.save()
            return render(request, 'tours/booking_success.html', {'tour': tour})
    else:
        form = BookingForm()
    return render(request, 'tours/book_tour.html', {'form': form, 'tour': tour})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'tours/booking_history.html', {'bookings': bookings})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'tours/profile.html', {'form': form, 'profile': profile})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('destination_list')
    else:
        form = UserCreationForm()
    return render(request, 'tours/signup.html', {'form': form})
