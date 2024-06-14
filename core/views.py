from django.shortcuts import render
from django.db.models import Sum, Prefetch
from django.utils import timezone
from .forms import RatingForm, RestaurantForm
from .models import Restaurant, Sale, Rating


# Create your views here.


def index(request):
    month_ago = timezone.now() - timezone.timedelta(days=20)
    sales = Prefetch("sales", queryset=Sale.objects.filter(datetime__gte=month_ago))
    # restaurants = Restaurant.objects.prefetch_related("sales", high_stars)
    restaurants = (
        Restaurant.objects.filter(ratings__rating__gte=3)
        .prefetch_related(sales, Prefetch("ratings"))
        .annotate(total=Sum("sales__income"))
    )
    print([r.total for r in restaurants])
    context = {"restaurants": restaurants}
    return render(request, "index.html", context)
