from rest_framework import viewsets, permissions
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# MovieViewSet: For CRUD operations on movies.
# Empty for the time being
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permissions_classes = [permissions.AllowAny]

# SeatViewSet: For seat availability and booking.
class SeatViewSet(viewsets.ModelViewSet): 
    queryset = Seat.objects.all() 
    serializer_class = SeatSerializer
    permissions_classes = [permissions.AllowAny]

# BookingViewSet: For users to book seats and view their booking history.
class BookingViewSet(viewsets.ModelViewSet): 
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer
    permissions_classes = [permissions.AllowAny]

    def create(self, serializer):
        booking = serializer.save()
        seat = booking.seat

    def delete(self, instance):
        seat = instance.seat
        super().perform_destory(instance)
        seat.booking_status = False
        seat.save(update_fields=['booking status'])