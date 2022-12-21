from datetime import date
from rest_framework import generics

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer

# ----
# Menu
# ----

class MenuList(generics.ListAPIView):
    queryset = Menu.objects.filter(actual_date=date.today())
    serializer_class = MenuSerializer

    
class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# ----------    
# Restaurant
# ----------

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer