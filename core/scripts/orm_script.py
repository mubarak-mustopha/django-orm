from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import F, Count, Q
from pprint import pprint as pp
import random


def run():
    r1 = Restaurant.objects.first()
    r2 = Restaurant.objects.last()

    r1.capacity = 10
    r2.capacity = 20
    r1.save()
    r2.save()

    print(Restaurant.objects.filter(capacity__isnull=False))

    pp(connection.queries)


# shell_plus --print-sql
