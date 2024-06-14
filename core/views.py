from django.shortcuts import render
from django.db.models import Sum, Prefetch
from django.utils import timezone
from .forms import RatingForm, RestaurantForm
from .models import Restaurant, Sale, Rating, StaffRestaurant


# Create your views here.


def index(request):
    jobs = StaffRestaurant.objects.prefetch_related("restaurant", "staff")

    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
    return render(request, "index.html")
