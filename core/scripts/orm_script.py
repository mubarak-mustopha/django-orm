from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower
from pprint import pprint as pp


def run():
    # many-to-many-managers all, add, remove, count, set(clears and overrides), clear
    staff, created = Staff.objects.get_or_create(name="John Wick")
    staff.restaurants.clear()
    restaurant = Restaurant.objects.first()
    restaurant2 = Restaurant.objects.last()

    staff.restaurants.add(restaurant, through_defaults={"salary": 28_500})
    # pp(connection.queries)


# 28:52

# shell_plus --print-sql
