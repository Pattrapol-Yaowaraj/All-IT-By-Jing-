from django.urls import path
from .views import Home, Display, editprofile

app_name = 'home'

urlpatterns = [
    path('', Home, name='Home'),
    path('display', Display, name='Display'),
    path('edit', editprofile, name='edit')
]
