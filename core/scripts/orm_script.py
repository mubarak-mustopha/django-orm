from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import F, Count, Q
from pprint import pprint as pp
import random


def run():
    rating = Rating.objects.first()
    print(rating.rating)
    rating.rating = F("rating") + 1
    rating.save()

    rating.refresh_from_db( )
    print(rating.rating)

    # pp(connection.queries)


# shell_plus --print-sql
