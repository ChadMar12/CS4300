from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, "bookings/base.html", {
        'TMDB_API_KEY': settings.TMDB_API_KEY
    })

def movie_list(request):
    return render(request, 'bookings/movie_list.html', {
        'TMDB_API_KEY': settings.TMDB_API_KEY
    })

def movie_detail(request, movie_id):
    # Render the same movie_list.html template
    # JavaScript will handle showing the detail view based on the URL
    return render(request, 'bookings/movie_list.html', {
        'TMDB_API_KEY': settings.TMDB_API_KEY,
        'movie_id': movie_id
    })

def booking_history(request):
    return render(request, 'bookings/booking_history.html', {
        'TMDB_API_KEY': settings.TMDB_API_KEY  # ADD THIS LINE
    })
def seat_booking(request):
    return render(request, 'bookings/seat_booking.html')