from datetime import date
from rest_framework import generics

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer



class MenuList(generics.ListAPIView):
    queryset = Menu.objects.filter(actual_date=date.today())
    serializer_class = MenuSerializer