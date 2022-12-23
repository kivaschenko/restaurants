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
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ultrices in iaculis nunc sed augue. Netus et malesuada fames ac turpis egestas. Egestas tellus rutrum tellus pellentesque eu. Elit duis tristique sollicitudin nibh sit amet commodo. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed velit. Amet commodo nulla facilisi nullam vehicula. Ut aliquam purus sit amet. Neque volutpat ac tincidunt vitae semper quis. Ut consequat semper viverra nam libero justo laoreet sit. Mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et. Tortor at risus viverra adipiscing at in. Mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing. Ac turpis egestas integer eget aliquet nibh praesent. Pellentesque habitant morbi tristique senectus et netus et. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Etiam non quam lacus suspendisse. In dictum non consectetur a erat nam. Sodales ut eu sem integer.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuVotesUpdateSerializer


class ResultsVotes(generics.ListAPIView):
    queryset = Menu.objects.filter(actual_date=date.today()).order_by('-votes').all()[:3]
    serializer_class = ResultVotesMenuTodaySerializer
    

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
