from django.db import models
from django.contrib.auth.models import User

#Create your models here
# tmdb_id grabs the id number of the movie from the tmdb api
# title, description, release_date, duration
class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    duration = models.TimeField()

    def __str__(self):
        return self.title

# movie, show date, show time
# theater name is the theater that the user picks and wants to see a movie at
class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater_name = models.CharField(max_length=100)
    show_date = models.DateField()
    show_time = models.TimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.theater_name} - {self.show_date} {self.show_time}"

# showing, seat number, booking status
# showing is the name of the movie from the tmdb api, this is to confirm that the seat the user wants is available
class Seat(models.Model):
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booking_status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('showing', 'seat_number')

    def __str__(self):
        return f"Seat {self.seat_number}"

# This is the booking system that will allow the user to purchase and confirm 
class Booking(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.seat}'