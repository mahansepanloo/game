from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('gamesmanager.urls')),
    path('shop/', include('shop.urls'))

]
