from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    short_name = models.CharField(max_length=60, db_index=True, unique=True)
    full_name = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    address = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="rests")

    class Meta:
        ordering = ["short_name"]

    def __str__(self) -> str:
        return f"{self.short_name}"

    def __repr__(self) -> str:
        return f"<Restaurant(id={self.id} short_name={self.short_name}...)>"


FOOD_TYPES = (
    ("salads", "Salads"),
    ("sandwiches", "Sandwiches"),
    ("snacks", "Snacks"),
    ("soups", "Soups"),
    ("wraps", "Wraps"),
)


class FoodItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FOOD_TYPES)

    class Meta:
        ordering = ["type", "name"]

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<FoodItem(id={self.id} name={self.name} type={self.type}...)>"


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")
    food_items = models.ManyToManyField(
        FoodItem,
        related_name="food_items",
    )
    actual_date = models.DateField()
    votes = models.IntegerField()

    class Meta:
        ordering = ["-actual_date"]
        unique_together = ["restaurant", "actual_date"]

    def __str__(self) -> str:
        return f"{self.id}: {self.actual_date}"

    def __repr__(self) -> str:
        return f"<Menu(id={self.id} restaurant={self.restaurant} actual_date={self.actual_date}...)>"
