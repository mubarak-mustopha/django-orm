from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import CharField, Value, Avg, Sum, Count
from pprint import pprint as pp
import random


def run():
    # group by all cols in restaurant table
    rs = Restaurant.objects.annotate(total_sales=Sum("sales__income")).filter(
        total_sales__lt=300
    )
    print(rs.aggregate(avg_sales=Avg("total_sales")))

    pp(connection.queries)


# shell_plus --print-sql
