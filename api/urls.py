from django.urls import path
from . import views
from .views import MyTokenObtainPairView, UserRegistrationView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]