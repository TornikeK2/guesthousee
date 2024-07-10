from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactInfoViewSet

router = DefaultRouter()
router.register(r'contact_info', ContactInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]