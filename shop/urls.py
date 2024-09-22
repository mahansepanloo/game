from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.ListShop.as_view(), name="shop_list"),
    path("buy/<int:id_item>", views.BuyItem.as_view(), name="shop_detail")
]
