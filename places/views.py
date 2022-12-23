from datetime import date
from rest_framework import generics

from .models import Restaurant, Menu, FoodItem
from .serializers import RestaurantSerializer, MenuSerializer, FoodItemSerializer, MenuVotesUpdate
from .permissions import IsAdminOrReadOnly, IsRestaurateurOrReadOnly

# ----
# Menu
# ----


class FoodItemList(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.filter(actual_date=date.today())
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsRestaurateurOrReadOnly,)

    
class MenuVoteView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuVotesUpdate


# ----------
# Restaurant
# ----------


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminOrReadOnly,)
