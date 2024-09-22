from django.contrib import admin
from .models import Shop,Item

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass