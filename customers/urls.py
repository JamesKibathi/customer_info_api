from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, LocationViewSet, BusinessViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'businesses', BusinessViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
