from django.urls import path
from .views import register, registration_success

app_name = 'registration'

urlpatterns = [
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
]
