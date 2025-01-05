import sys
from functools import partial

from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import Sum, Prefetch
from django.utils import timezone
from .forms import RatingForm, RestaurantForm, OrderForm
from .models import Restaurant, Sale, Rating, StaffRestaurant


# Create your views here.


def index(request):
    jobs = StaffRestaurant.objects.prefetch_related("restaurant", "staff")

    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
    return render(request, "index.html")


def send_email(email):
    print(f"Dear {email}, your order has been placed.")


def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()

                order.product.in_stock -= order.quantity
                order.product.save()
            transaction.on_commit(
                partial(send_email, "mubaarock021@gmail.com"),
            )
            return redirect("place_order")
        else:
            return render(request, "order.html", {"form": form})

    return render(request, "order.html", {"form": OrderForm()})
