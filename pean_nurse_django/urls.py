from django.urls import path, include
from rest_framework import routers
from .views.user_views import UserViewSet
from .views.auth_views import AuthView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth', AuthView.as_view())
]
