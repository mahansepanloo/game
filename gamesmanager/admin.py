from django.contrib import admin
from .models import *


@admin.register(Bottle)
class BAdmin(admin.ModelAdmin):
    pass