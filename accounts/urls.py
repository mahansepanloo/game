from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("log",Login.as_view(),name="login"),
    path("sign",RegisterView.as_view())

]
