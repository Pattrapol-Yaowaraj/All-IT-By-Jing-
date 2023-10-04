from django.urls import path
from .views import Home, Display

urlpatterns = [
    path('', Home),
    path('display', Display),
]
