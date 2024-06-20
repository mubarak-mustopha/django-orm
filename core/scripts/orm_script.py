from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import F
from pprint import pprint as pp
import random


def run():
    sales = Sale.objects.annotate(profit=F("income") - F("expenditure")).values(
        "income",
        "expenditure",
        "profit",
    )
    print(sales[0])
    pp(connection.queries)


# shell_plus --print-sql
