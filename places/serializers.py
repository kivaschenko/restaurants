from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            "id",
            "short_name",
            "full_name",
            "description",
            "lng",
            "lat",
            "address",
        )


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "restaurant", "body", "actual_date", "votes")
