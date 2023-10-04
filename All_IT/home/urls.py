from django.urls import path
from .views import Home, Display, Signup

urlpatterns = [
    path('', Home),
    path('display', Display),
    path('signup', Signup),
]
