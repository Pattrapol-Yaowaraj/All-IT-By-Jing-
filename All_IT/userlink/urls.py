from django.urls import path
from . import views

urlpatterns = [
    path('input_link/', views.input_link, name='input_link'),
    path('display_links/', views.display_links, name='display_links'),
]