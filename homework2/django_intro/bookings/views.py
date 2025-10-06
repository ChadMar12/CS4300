from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view , permission_classes 
from django.db import transaction
from .models import Movie, Showing, Seat, Booking
from .serializers import MovieSerializer, ShowingSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import AllowAny
import datetime

# >>> ADDED IMPORTS (minimal) <<<
from django.contrib.auth.models import User   # NEW
import os                                     # NEW

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class ShowingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Showing.objects.all()
    serializer_class = ShowingSerializer
    permission_classes = [permissions.AllowAny]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=False, methods=['get'])
    def by_showing(self, request):
        """Get all seats for a specific showing: /api/seats/by_showing/?showing_id=1"""
        showing_id = request.query_params.get('showing_id')
        if not showing_id:
            return Response({'error': 'showing_id required'}, status=status.HTTP_400_BAD_REQUEST)
        
        seats = Seat.objects.filter(showing_id=showing_id)
        serializer = self.get_serializer(seats, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def perform_create(self, serializer):
        # >>> ADDED: fallback user for anonymous visitors <<<
        fallback_username = os.getenv("BOOKING_GUEST_USERNAME", "guest")
        user = (
            self.request.user
            if self.request.user.is_authenticated
            else User.objects.get_or_create(username=fallback_username, defaults={"is_active": True})[0]
        )
        # -----------------------------------------------

        seat = serializer.validated_data["seat"]
        if seat.booking_status:
            raise ValueError("Seat is already booked.")
        booking = serializer.save(user=user)   # <<< ADDED: attach user to the booking
        seat.booking_status = True
        seat.save(update_fields=["booking_status"])
        return booking

    def perform_destroy(self, instance):
        seat = instance.seat
        super().perform_destroy(instance)
        seat.booking_status = False
        seat.save(update_fields=["booking_status"])


@api_view(['POST'])
@permission_classes([AllowAny])
def get_or_create_showing(request):
    """
    Create or fetch a showing for booking.
    Expects: tmdb_id, title, theater, show_date, show_time
    Returns: showing_id
    """
    tmdb_id = request.data.get('tmdb_id')
    title = request.data.get('title')
    theater = request.data.get('theater')
    show_date = request.data.get('show_date')
    show_time = request.data.get('show_time')
    
    if not all([tmdb_id, title, theater, show_date, show_time]):
        return Response({'error': 'Missing required fields'}, status=400)
    
    # Get or create movie
    movie, created = Movie.objects.get_or_create(
        tmdb_id=tmdb_id,
        defaults={
            'title': title,
            'description': request.data.get('description', ''),
            'duration': datetime.time(2, 0, 0)
        }
    )
    
    # Get or create showing
    showing, showing_created = Showing.objects.get_or_create(
        movie=movie,
        theater_name=theater,
        show_date=show_date,
        show_time=show_time
    )
    
    # If newly created, generate seats using bulk_create for performance
    if showing_created:
        seats = []
        for row in range(1, 11):
            for col in range(1, 17):
                row_letter = chr(64 + row)
                seat_label = f"{row_letter}{col}"
                seats.append(Seat(
                    showing=showing,
                    seat_number=seat_label,
                    booking_status=False
                ))
        # Use bulk_create - one database query instead of 160!
        Seat.objects.bulk_create(seats)
    
    return Response({
        'showing_id': showing.id,
        'movie_id': movie.id,
        'seats_created': showing_created
    })