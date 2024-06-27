from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat, Coalesce
from django.db.models import F, Count, Q, Sum, Avg, Case, When, Value, Max, Min
from pprint import pprint as pp
import random


def run():

    rating_stats = Rating.objects.aggregate(
        avg=Avg("rating"), max=Max("rating"), min=Min("rating")
    )
    rs = Restaurant.objects.annotate(
        avg_rating=Avg("ratings__rating"),
        num_rating=Count("ratings"),
    )
    rs = rs.annotate(
        rating_rank=Case(
            When(
                avg_rating__gt=rating_stats["avg"], num_rating__gt=1, then=Value("High")
            ),
            When(
                avg_rating__range=(2, rating_stats["avg"]),
                num_rating__gt=1,
                then=Value("Moderate"),
            ),
            When(
                avg_rating__lt=2,
                num_rating__gt=1,
                then=Value("Low"),
            ),
            default=None,
        )
    )

    print(rs.values("avg_rating", "num_rating", "rating_rank"))
    # pp(connection.queries)


# shell_plus --print-sql
