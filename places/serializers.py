from rest_framework import serializers
from .models import Restaurant, Menu, FoodItem


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    menus = serializers.StringRelatedField(many=True)
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
            "menus",
        )

    def validate(self, attrs):
        user = self.context['request'].user
        attrs.update({"admin": user})
        return attrs

    def create(self, validated_data):
        restaurant = Restaurant.objects.create(**validated_data)
        restaurant.save()
        return restaurant


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["name", "description", "type"]


class MenuSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True)
    restaurant_id = serializers.IntegerField()

    class Meta:
        model = Menu
        fields = ("id", "restaurant_id", "food_items", "actual_date")

    def validate(self, attrs):
        print('attrs:', attrs)
        return super().validate(attrs)

    def create(self, validate_data):
        food_items_objects = []
        food_item_list = validate_data.pop('food_items')
        for dict_ in food_item_list:
            food_item, created = FoodItem.objects.get_or_create(**dict_)
            food_items_objects.append(food_item)
        restaurant_id = validate_data.pop('restaurant_id')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        menu = Menu.objects.create(restaurant=restaurant, actual_date=validate_data['actual_date'], votes=0)
        menu.save()
        menu.food_items.set(food_items_objects)
        return menu