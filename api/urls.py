from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('admin', views.AdminViewSet)
router.register('site', views.SiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]