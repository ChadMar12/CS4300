from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Movie, Seat, Booking


# Create your views here.

#MovieViewSet: For CRUD operations on movies.
#Empty for the time being
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    
    def create(self, request) :
        pass 

    def read(self, request):
        pass

    def update(self, request):
        pass
    
    def destroy(self, request):
        pass
    
#SeatViewSet: For seat availability and booking.
class SeatViewSet():
    
    def seat_availability():
        pass
    
    def book_seat():
        pass
 

#BookingViewSet: For users to book seats and view their booking history.
class BookingViewSet():

    def book_seat():
        pass
    
    def view_seat():
        pass