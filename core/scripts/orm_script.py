from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import F
from pprint import pprint as pp
import random


def run():
    sales = Sale.objects.filter(expenditure__gt=F("income")).values(
        "income", "expenditure"
    )
    print(sales)
    pp(connection.queries)


# shell_plus --print-sql
