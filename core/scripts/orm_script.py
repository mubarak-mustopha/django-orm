from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import F, Count, Q
from pprint import pprint as pp
import random


def run():
    # Find Sales where
    #   - profit is greater than expenditure , OR
    #   - restaurant name contains a number
    profits = Q(income__gt=F("expenditure"))
    has_num = Q(restaurant__name__regex=r"[0-9]+")

    sales = Sale.objects.filter(has_num | profits)

    print(
        sales.values(
            "restaurant__name",
            "income",
            "expenditure",
        )
    )
    pp(connection.queries)


# shell_plus --print-sql
