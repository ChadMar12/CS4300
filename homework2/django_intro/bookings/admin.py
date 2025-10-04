from django.contrib import admin
from .models import Movie, Showing, Seat, Booking

# Register your models here

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'tmdb_id', 'release_date', 'duration')

@admin.register(Showing)
class ShowingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theater_name', 'show_date', 'show_time')
    
    # Since we are using a api for learning purposes, this function will create the movie theater's seats
    # The seats will be added to the Django database on a as needed basis.
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        if not change:
            for row in range(1, 11):
                for col in range(1, 17):
                    row_letter = chr(64 + row)
                    seat_label = f"{row_letter}{col}"
                    Seat.objects.create(
                        showing=obj,
                        seat_number=seat_label,
                        booking_status=False
                    )

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'showing', 'booking_status')
    list_filter = ('booking_status', 'showing')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'seat', 'booking_date')