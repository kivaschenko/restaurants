from django.contrib import admin
from .models import Restaurant, Menu, FoodItem


admin.site.register(Restaurant)
admin.site.register(FoodItem)
admin.site.register(Menu)
