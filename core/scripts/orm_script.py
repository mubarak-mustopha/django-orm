from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper
from pprint import pprint as pp
import random


def run():
    IT = Restaurant.TypeChoices.ITALIAN
    ratings = Rating.objects.filter(restaurant__restaurant_type=IT).values(
        "rating", "restaurant__name"
    )
    print(ratings) 
    pp(connection.queries)


# shell_plus --print-sql
