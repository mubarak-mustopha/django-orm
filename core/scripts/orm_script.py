from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower
from pprint import pprint as pp
import random


def run():
    # many-to-many-managers all, add, remove, count, set(clears and overrides), clear
    staff, created = Staff.objects.get_or_create(name="John Wick")

    staff.restaurants.set(
        Restaurant.objects.all()[:10],
        through_defaults={"salary": random.randint(20_000, 80_000)},
    )


# 28:52

# shell_plus --print-sql
