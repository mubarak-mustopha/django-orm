from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import CharField, Value, Avg, Sum, Count
from pprint import pprint as pp
import random


def run():
    # group by all cols in restaurant table
    rs = Restaurant.objects.annotate(
        num_ratings=Count("ratings"),
        avg_rating=Avg("ratings__rating"),
    )
    print(rs.values("name", "num_ratings", "avg_rating"))

    # group by single column
    rs = Restaurant.objects.values("restaurant_type").annotate(
        avg_rating=Avg("ratings__rating"),
    )
    print(rs)
    pp(connection.queries)


# shell_plus --print-sql
