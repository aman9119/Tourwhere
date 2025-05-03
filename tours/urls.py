from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('tours/', views.tour_list, name='tour_list'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tours/<int:tour_id>/book/', views.book_tour, name='book_tour'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='tours/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('bookings/', views.booking_history, name='booking_history'),
    path('profile/', views.profile, name='profile'),
]
