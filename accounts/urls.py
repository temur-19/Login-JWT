from django.urls import path
from accounts.SignUp.api_endpoints.SignUp.views import signup
from accounts.Login.api_endpoints.Login.views import get_profile, login
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/',login, name='login'),
    path('signup/',signup, name='signup'),
    path('login/me', get_profile, name='get_profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]