from django.urls import path

from places import views


urlpatterns = [
    path("food-items/", views.FoodItemList.as_view()),
    path("menus/", views.MenuList.as_view(), name='menu-list'),
    path("menus/<int:pk>/", views.MenuDetail.as_view()),
    path("restaurants/", views.RestaurantList.as_view()),
    path("restaurants/<int:pk>/", views.RestaurantDetail.as_view()),
]
