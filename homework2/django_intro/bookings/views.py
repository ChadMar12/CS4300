from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer


# Create your views here.

#MovieViewSet: For CRUD operations on movies.
#Empty for the time being
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Movie.objets.all()
    serializers_class = ModelSerializer

    def create(self, request):
        pass
    
    def update(self, request, pk=None):
        pass
    
    def read(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass

#SeatViewSet: For seat availability and booking.
class SeatViewSet():
    
    queryset = Movie.objets.all()
    serializers_class = SeatSerializer
     

#BookingViewSet: For users to book seats and view their booking history.
class BookingViewSet():

    queryset = Movie.objets.all()
    serializers_class = BookingSerializer