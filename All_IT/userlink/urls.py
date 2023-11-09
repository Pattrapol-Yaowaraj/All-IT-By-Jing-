from django.urls import path
from . import views

app_name = 'userlink'

urlpatterns = [
    path('userlink/<str:user_sid>/', views.userlink, name='userlink'),
    path('userlink/<int:link_id>/delete/', views.delete_link, name='delete_link'),
]