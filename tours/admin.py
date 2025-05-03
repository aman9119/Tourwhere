from django.contrib import admin
from .models import Destination, Tour, Booking, Profile, Review
from django.utils.html import format_html

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'image_preview')
    search_fields = ('name', 'country')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;" />', obj.image.url)
        return ""
    image_preview.short_description = 'Image'

class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'start_date', 'end_date', 'price')
    search_fields = ('title', 'destination__name')
    list_filter = ('destination',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name', 'email', 'num_people', 'booking_date', 'user')
    search_fields = ('name', 'email', 'tour__title')
    list_filter = ('tour', 'user')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview', 'bio')
    search_fields = ('user__username',)
    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="height:40px; border-radius:50%;" />', obj.avatar.url)
        return ""
    avatar_preview.short_description = 'Avatar'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('tour', 'user', 'rating', 'created_at')
    search_fields = ('tour__title', 'user__username', 'comment')
    list_filter = ('tour', 'rating')

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Review, ReviewAdmin)

# Register your models here.
