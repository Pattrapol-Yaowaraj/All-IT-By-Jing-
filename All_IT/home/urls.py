from django.urls import path
from .views import Home, Display

app_name = 'home'

urlpatterns = [
    path('', Home, name='Home'),
    path('display', Display, name='Display'),
]
