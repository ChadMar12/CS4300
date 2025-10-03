from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import view_pages  # Add this import

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

app_name = 'bookings'

urlpatterns = [
    # API routes
    path('api/', include(router.urls)),
    
    # Regular template views (using views_pages)
    path('', view_pages.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', view_pages.movie_detail, name='movie_detail'),
    path('booking-history/', view_pages.booking_history, name='booking_history'),
    path('seat-booking/', view_pages.seat_booking, name='seat_booking'),
]