# from rest_framework import viewsets, permissions
# from .models import Movie, Seat, Booking
# from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# # MovieViewSet: For CRUD operations on movies.
# # Empty for the time being
# class MovieViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     permissions_classes = [permissions.AllowAny]

# # SeatViewSet: For seat availability and booking.
# class SeatViewSet(viewsets.ModelViewSet): 
#     queryset = Seat.objects.all() 
#     serializer_class = SeatSerializer
#     permissions_classes = [permissions.AllowAny]

# # BookingViewSet: For users to book seats and view their booking history.
# class BookingViewSet(viewsets.ModelViewSet): 
#     queryset = Booking.objects.all() 
#     serializer_class = BookingSerializer
#     permissions_classes = [permissions.AllowAny]

#     def create(self, serializer):
#         booking = serializer.save()
#         seat = booking.seat

#     def delete(self, instance):
#         seat = instance.seat
#         super().perform_destory(instance)
#         seat.booking_status = False
#         seat.save(update_fields=['booking status'])

# bookings/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db import transaction
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def perform_create(self, serializer):
        seat = serializer.validated_data["seat"]
        if seat.booking_status:
            # prevent double-booking
            raise ValueError("Seat is already booked.")
        booking = serializer.save()
        seat.booking_status = True
        seat.save(update_fields=["booking_status"])
        return booking

    def perform_destroy(self, instance):
        seat = instance.seat
        super().perform_destroy(instance)
        seat.booking_status = False
        seat.save(update_fields=["booking_status"])
