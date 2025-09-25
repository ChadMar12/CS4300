from django.db import models

# Movie, Seat, and Booking

# Create your models here.

# Movie: title, description, release date, duration.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateTimeField("date published")
    duration = models.TimeField()

#Seat: seat number, booking status.
class Seat(models.Model):
    seat_number = models.PositiveIntegerField()
    booking_status = models.BooleanField(default=False)

#Booking: movie, seat, user, booking date
class Booking(models.Model):
    movie = models.CharField(max_length=200)
    seat = models.PositiveIntegerField()
    user = models.CharField(max_length=200)
    booking_date = models.DateTimeField()


# will import this once I need it 

# class Booking(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     booking_date = models.DateTimeField(auto_now_add=True)

