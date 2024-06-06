from django import forms
from .models import Rating, Restaurant


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")
