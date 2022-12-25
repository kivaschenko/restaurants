from datetime import date
from rest_framework import generics

from .models import Restaurant, Menu, FoodItem
from .serializers import (
    RestaurantSerializer, 
    MenuSerializer, 
    FoodItemSerializer, 
    MenuVotesUpdateSerializer, 
    ResultVotesMenuTodaySerializer,
)
from .permissions import IsAdminOrReadOnly, IsRestaurateurOrReadOnly

# ----
# Menu
# ----


class FoodItemList(generics.ListCreateAPIView):
    '''These endpoints are for return food items list by GET and create a new food item by POST.'''
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class MenuList(generics.ListCreateAPIView):
    '''These endpoints are for return list of all menus for today by GET. And to create a new menu instance by POST.'''
    queryset = Menu.objects.filter(actual_date=date.today())
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    '''These endpoints to retrieve current menu by GET, to update meny by PUT, PATCH. And to delete menu by DELETE.
    Permissions are only for user which is admin of current restaurant.'''
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsRestaurateurOrReadOnly,)


class MenuVoteView(generics.UpdateAPIView):
    """This endpoint is to add votes for current menu."""
    queryset = Menu.objects.all()
    serializer_class = MenuVotesUpdateSerializer


class ResultsVotes(generics.ListAPIView):
    '''This endpoint is to get results of vote at today. Return the list of first 3 menus ordered by descend.'''
    queryset = Menu.objects.filter(actual_date=date.today()).order_by('-votes').all()[:3]
    serializer_class = ResultVotesMenuTodaySerializer
    

# ----------
# Restaurant
# ----------


class RestaurantList(generics.ListCreateAPIView):
    '''These endpoints are to get list of all restaurants by GET. And to create a new restaurant by POST.'''
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    '''These endpoints are to retrieve the restaurant by GET, to update the restaurant by PUT, PATCH, and to delete 
    the restaurant by DELETE.'''
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminOrReadOnly,)
