from django.contrib import admin
from django.urls import path, include
from production.views import PalletsViewSet, BoxsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pallet', PalletsViewSet, basename='Pallet')
router.register('box', BoxsViewSet, basename='Box')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
