from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Upper, Length, Concat, Coalesce
from django.db.models import F, Count, Q, Sum, Avg
from pprint import pprint as pp
import random


def run():

    print(Restaurant.objects.annotate(pname=Coalesce("pka", "name")).values("pname"))

    pp(connection.queries)


# shell_plus --print-sql
