from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat, Coalesce
from django.db.models import F, Count, Q, Sum, Avg
from pprint import pprint as pp
import random


def run():

    print(
        Rating.objects.filter(rating__lt=0).aggregate(
            avg_rating=Coalesce(Sum("rating"), 0)
        )
    )

    print(Restaurant.objects.aggregate(total_cap=Sum("capacity", default=0)))
    pp(connection.queries)


# shell_plus --print-sql
