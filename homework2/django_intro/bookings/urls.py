from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'showings', views.ShowingViewSet, basename='showing')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('get-or-create-showing/', views.get_or_create_showing, name='get-or-create-showing'),
    path('', include(router.urls)),
]