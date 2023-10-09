from django.urls import path
from .views import register, registration_success, validate_credentials



app_name = 'registration'

urlpatterns = [
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
    path('validate_credentials/', validate_credentials, name='validate_credentials'),
]
