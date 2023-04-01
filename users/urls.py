from django.urls import path
from dj_rest_auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-keys/', views.APIKeysView.as_view(), name='api-keys'),
    path('validate-api-keys/', views.ValidateAPIKeys.as_view(), name='validate-api-keys')
]
