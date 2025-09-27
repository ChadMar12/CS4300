# bookings/views_pages.py  (new file)
from django.shortcuts import render

def home(request):
    
    # You can pass context later if you want
    return render(request, "bookings/base.html")