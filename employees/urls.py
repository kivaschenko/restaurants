from django.urls import path

from .views import CreateUserView, CreateEmployeeView


urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("employees/", CreateEmployeeView.as_view()),
]