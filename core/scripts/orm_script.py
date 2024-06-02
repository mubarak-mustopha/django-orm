from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint as pp


def run():

    user = User.objects.first()
    restaurant = Restaurant.objects.get(id=2)

    rating = Rating(
        user=user,
        restaurant=restaurant,
        rating=9,
    )

    rating.full_clean()
    rating.save()

    pp(connection.queries)


# shell_plus --print-sql