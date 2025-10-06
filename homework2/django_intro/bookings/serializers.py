from rest_framework import serializers
from .models import Movie, Showing, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# Added showing as for a learning experice with using API's
class ShowingSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    
    class Meta:
        model = Showing
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    showing_id = serializers.IntegerField(source='showing.id', read_only=True)
    movie_title = serializers.CharField(source='showing.movie.title', read_only=True)
    
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True)
    movie_title = serializers.CharField(source='seat.showing.movie.title', read_only=True)
    showing_id = serializers.IntegerField(source='seat.showing.id', read_only=True)  # Add this line
    
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('user',)