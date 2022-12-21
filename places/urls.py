from django.urls import path

from .views import MenuList


urlpatterns = [
    path('menus/', MenuList.as_view()),
]
