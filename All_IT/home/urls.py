from django.urls import path
from .views import Home, Display, editprofile, Delete

app_name = 'home'

urlpatterns = [
    path('', Home, name='Home'),
    path('display', Display, name='Display'),
    path('edit', editprofile, name='edit'),
    path('delete', Delete, name='Delete')
]
