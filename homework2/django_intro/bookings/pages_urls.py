# bookings/pages_urls.py
from django.urls import path
from . import view_pages

app_name = "bookings"

urlpatterns = [
    path("", view_pages.home, name="home"),
    path("movies/", view_pages.movie_list, name="movie_list"),
    path("movie/<int:movie_id>/", view_pages.movie_detail, name="movie_detail"),
    path("seat-booking/", view_pages.seat_booking, name="seat_booking"),
    path("history/", view_pages.booking_history, name="booking_history"),
]