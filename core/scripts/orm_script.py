from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat, Coalesce
from django.db.models import F, Count, Q, Sum, Avg, Case, When, Value, Max, Min
from pprint import pprint as pp
import random


def run():

    types = Restaurant.TypeChoices
    continent_to_country = {
        "Asia": [types.CHINESE, types.INDIAN],
        "America": [types.MEXICAN],
        "Europe": [types.ITALIAN, types.GREEK],
    }

    rs = Restaurant.objects.annotate(
        continent=Case(
            When(restaurant_type__in=continent_to_country["Asia"], then=Value("Asia")),
            When(
                restaurant_type__in=continent_to_country["America"],
                then=Value("America"),
            ),
            When(
                restaurant_type__in=continent_to_country["Europe"], then=Value("Europe")
            ),
            default=Value("Not Specific"),
        )
    )
    print(rs.values("restaurant_type", "continent"))

    # pp(connection.queries)


# shell_plus --print-sql
