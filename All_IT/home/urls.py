from django.urls import path
from .views import Home, Display, Editprofile, Delete, Logout

app_name = 'home'

urlpatterns = [
    path('', Home, name='Home'),
    path('display', Display, name='Display'),
    path('edit', Editprofile, name='edit'),
    path('delete', Delete, name='Delete'),
    path('logout', Logout, name='Logout')
]
