from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import F, Count, Q
from pprint import pprint as pp
import random


def run():
    r = Restaurant.objects.order_by(F("capacity").asc(nulls_last=True)).values(
        "name", "capacity"
    )
    print(r)
    pp(connection.queries)


# shell_plus --print-sql
