from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat, Coalesce
from django.db.models import F, Count, Q, Sum, Avg, Case, When
from pprint import pprint as pp
import random


def run():
    # EX 1

    # it = Restaurant.TypeChoices.ITALIAN

    # rs = Restaurant.objects.annotate(
    #     is_italian=Case(
    #         When(restaurant_type=it, then=True),
    #         default=False,
    #     )
    # )

    # EX 2
    # rs = Restaurant.objects.annotate(num_sales=Count("sales"))

    # rs = rs.annotate(
    #     high_sales=Case(
    #         When(num_sales__gte=8, then=True),
    #         default=False,
    #     ),
    # )

    # print(rs.values_list("num_sales", "high_sales"))

    # Restaurant average rating > 3.5
    # Restaurant has more than 1 rating
    # print(Rating.objects.values("rating"))
    rs = Restaurant.objects.annotate(
        avg_rating=Avg("ratings__rating"),
        num_rating=Count("ratings"),
    )
    rs = rs.annotate(
        highly_rated=Case(
            When(
                (Q(avg_rating__gt=3.5) & Q(num_rating__gt=1)),
                then=True,
            ),
            default=False,
        )
    )

    print(rs.values("avg_rating", "num_rating", "highly_rating "))
    # pp(connection.queries)


# shell_plus --print-sql
