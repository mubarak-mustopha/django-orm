from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper
from pprint import pprint as pp
import random


def run():
    restaurants = Restaurant.objects.values_list("name", flat=True)

    print(restaurants)
    # pp(connection.queries)


# shell_plus --print-sql
