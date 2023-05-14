from django.urls import path
from .views import MyTokenObtainPairView,RegisterView,LoginView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',RegisterView.as_view(),name='sign-up'),
    path('login/',LoginView.as_view(),name='login-user'),
]