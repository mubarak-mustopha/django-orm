from django import forms
from .models import Rating, Restaurant, Order


class OutOfStockException(Exception):
    pass


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "quantity"]

    def save(self, commit=True):
        order = super().save(commit=False)
        if order.quantity > order.product.in_stock:
            raise OutOfStockException(
                f"Not enough item in stock for product: {order.product}"
            )
        if commit:
            order.save()
        return order


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")
