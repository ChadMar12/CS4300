from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Showing, Seat, Booking
import datetime

# ==============================================================================
#                               Unit Tests
# ==============================================================================

# Testing Movie model
class MovieModelTest(TestCase):

    # Creating a test movie
    def setUp(self):

        self.movie = Movie.objects.create(
            tmdb_id=550,
            title="Fight Club",
            description="What happens in fight club statys in fight club.",
            duration=datetime.time(2, 19, 0)
        )
    
    # Testing if the movie was created properly
    def test_movie_creation(self):

        self.assertEqual(self.movie.title, "Fight Club")
        self.assertEqual(self.movie.tmdb_id, 550)
        self.assertIsNotNone(self.movie.release_date)

    
# Testing Shwoing model
class ShowingModelTest(TestCase):
    
    def setUp(self):

        self.movie = Movie.objects.create(
            tmdb_id=278,
            title="The Shawshank Redemption",
            description="Two imprisoned men bond over years.",
            duration=datetime.time(2, 22, 0)
        )

        # Setting up a movie showing
        self.showing = Showing.objects.create(
            movie=self.movie,
            theater_name="The Grand Picture Palace",
            show_date=datetime.date(2025, 10, 15),
            show_time=datetime.time(19, 30, 0)
        )
    
    # Testing to see if the showing was created
    def test_showing_creation(self):
        self.assertEqual(self.showing.theater_name, "The Grand Picture Palace")
        self.assertEqual(self.showing.movie, self.movie)

# Testing Seat model
class SeatModelTest(TestCase):
    
    def setUp(self):

        self.movie = Movie.objects.create(
            tmdb_id=680,
            title="Pulp Fiction",
            description="Various interconnected stories.",
            duration=datetime.time(2, 34, 0)
        )

        self.showing = Showing.objects.create(
            movie=self.movie,
            theater_name="The Stellar Screen",
            show_date=datetime.date(2025, 10, 20),
            show_time=datetime.time(20, 0, 0)
        )

        # Choosing a seat to test
        self.seat = Seat.objects.create(
            showing=self.showing,
            seat_number="A5",
            booking_status=False
        )
    
    # Testing to see if the seat was created
    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A5")
        self.assertFalse(self.seat.booking_status)
    
    # Testing to see if after we pick seat A5 that other seats llke B3 are available
    def test_seat_booking_status_default(self):
        new_seat = Seat.objects.create(
            showing=self.showing,
            seat_number="B3"
        )
        self.assertFalse(new_seat.booking_status)

# Testing Booking model
class BookingModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.movie = Movie.objects.create(
            tmdb_id=13,
            title="Forrest Gump",
            description="Life story of Forrest Gump.",
            duration=datetime.time(2, 22, 0)
        )

        self.showing = Showing.objects.create(
            movie=self.movie,
            theater_name="The Flicker House",
            show_date=datetime.date(2025, 10, 25),
            show_time=datetime.time(18, 0, 0)
        )

        self.seat = Seat.objects.create(
            showing=self.showing,
            seat_number="C7",
            booking_status=False
        )

        # Creating a booking for the user
        self.booking = Booking.objects.create(
            seat=self.seat,
            user=self.user
        )
    
    # Testing to see if the booking was created
    def test_booking_creation(self):

        self.assertEqual(self.booking.user.username, 'testuser')
        self.assertEqual(self.booking.seat.seat_number, "C7")
        self.assertIsNotNone(self.booking.booking_date)

# ==============================================================================
#                            Integration Tests
# ==============================================================================

# Testing Movie api
class MovieAPITest(APITestCase):
    
    def setUp(self):
        self.movie = Movie.objects.create(
            tmdb_id=238,
            title="The Godfather",
            description="The aging patriarch of a crime dynasty.",
            duration=datetime.time(2, 55, 0)
        )
    
    # Testing the movie_list page to ensure that it loads
    def test_get_movie_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Godfather")
    
    # Testing the movie detail page to ensure that it loads
    def test_get_movie_detail(self):
        response = self.client.get(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "The Godfather")
        self.assertEqual(response.data['tmdb_id'], 238)

# Test for the Shwoing API
class ShowingAPITest(APITestCase):
    
    def setUp(self):
        self.movie = Movie.objects.create(
            tmdb_id=424,
            title="Schindler's List",
            description="Story of Oskar Schindler.",
            duration=datetime.time(3, 15, 0)
        )

        self.showing = Showing.objects.create(
            movie=self.movie,
            theater_name="Marquee Dreams Cinema",
            show_date=datetime.date(2025, 11, 1),
            show_time=datetime.time(19, 0, 0)
        )
    
    # Testing to see if we can view the showings and times 
    def test_get_showing_list(self):
        response = self.client.get('/api/showings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    # Getting the showing times
    def test_get_showing_detail(self):
        response = self.client.get(f'/api/showings/{self.showing.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['theater_name'], "Marquee Dreams Cinema")
        self.assertEqual(response.data['movie_title'], "Schindler's List")

# Testing Seat API
class SeatAPITest(APITestCase):
    
    def setUp(self):
        self.movie = Movie.objects.create(
            tmdb_id=155,
            title="The Dark Knight",
            description="Batman faces the Joker.",
            duration=datetime.time(2, 32, 0)
        )

        self.showing = Showing.objects.create(
            movie=self.movie,
            theater_name="The Reel Escape",
            show_date=datetime.date(2025, 11, 5),
            show_time=datetime.time(20, 30, 0)
        )

        self.seat = Seat.objects.create(
            showing=self.showing,
            seat_number="D8",
            booking_status=False
        )
    
    # Testing to see if we can get seats 
    def test_get_seats_by_showing(self):
        response = self.client.get(f'/api/seats/by_showing/?showing_id={self.showing.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seat_number'], "D8")
    
# Testing Booking API
class BookingAPITest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='apiuser',
            password='apipass123'
        )

        self.movie = Movie.objects.create(
            tmdb_id=389,
            title="12 Angry Men",
            description="Jury deliberates a murder case.",
            duration=datetime.time(1, 36, 0)
        )

        self.showing = Showing.objects.create(
            movie=self.movie,
            theater_name="The Grand Picture Palace",
            show_date=datetime.date(2025, 11, 10),
            show_time=datetime.time(17, 0, 0)
        )

        self.seat = Seat.objects.create(
            showing=self.showing,
            seat_number="E5",
            booking_status=False
        )
    
    # Testing to seee if when the user clicks to purchase seats the API will create a booking
    def test_create_booking(self):

        data = {
            'seat': self.seat.id,
            'user': self.user.id
        }

        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)
    
    # Tesing to see if we can view our booking history
    def test_get_booking_list(self):

        Booking.objects.create(seat=self.seat, user=self.user)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    # Testing if we can delete our booking history. This feature is for homework an demo purpose
    def test_delete_booking(self):

        booking = Booking.objects.create(seat=self.seat, user=self.user)
        self.seat.booking_status = True
        self.seat.save()

        response = self.client.delete(f'/api/bookings/{booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# Testing to see if we can get and create a showing when the user clicks on a movie
class GetOrCreateShowingAPITest(APITestCase):
    
    # Test for showing the seats
    def test_create_new_showing_with_seats(self):
        data = {
            'tmdb_id': 599,
            'title': 'The Matrix',
            'description': 'A hacker discovers reality is a simulation.',
            'theater': 'The Stellar Screen',
            'show_date': '2025-11-15',
            'show_time': '21:00:00'
        }
        response = self.client.post('/api/get-or-create-showing/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('showing_id', response.data)
        self.assertTrue(response.data['seats_created'])
        
        # Verify seats were created
        showing_id = response.data['showing_id']
        seat_count = Seat.objects.filter(showing_id=showing_id).count()
        self.assertEqual(seat_count, 160) 
    
    # Test to see if we can see showings that are created
    def test_get_existing_showing(self):
        data = {
            'tmdb_id': 120,
            'title': 'The Lord of the Rings',
            'description': 'Epic fantasy adventure.',
            'theater': 'The Flicker House',
            'show_date': '2025-11-20',
            'show_time': '18:30:00'
        }
        
        # First request
        response1 = self.client.post('/api/get-or-create-showing/', data, format='json')
        showing_id_1 = response1.data['showing_id']
        
        # Second request with same data
        response2 = self.client.post('/api/get-or-create-showing/', data, format='json')
        showing_id_2 = response2.data['showing_id']
        
        # Should return same showing
        self.assertEqual(showing_id_1, showing_id_2)
        self.assertFalse(response2.data['seats_created'])
    
