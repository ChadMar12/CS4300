# bookings/pages_urls.py
from django.urls import path
from django.views.generic import TemplateView

app_name = "bookings"  # lets you use {% url 'bookings:movie_list' %} in templates

urlpatterns = [

    path("", TemplateView.as_view(template_name="bookings/base.html"), name="home"),

    path("movies/",        TemplateView.as_view(template_name="bookings/movie_list.html"),     name="movie_list"),
    path("seat-booking/",  TemplateView.as_view(template_name="bookings/seat_booking.html"),   name="seat_booking"),
    path("history/",       TemplateView.as_view(template_name="bookings/booking_history.html"),name="booking_history"),
]
