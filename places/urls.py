from django.urls import path

from .views import MenuList, MenuDetail, RestaurantList, RestaurantDetail


urlpatterns = [
    path("menus/", MenuList.as_view()),
    path("menus/<int:pk>/", MenuDetail.as_view()),
    path("restaurants/", RestaurantList.as_view()),
    path("restaurants/<int:pk>/", RestaurantDetail.as_view()),
]
