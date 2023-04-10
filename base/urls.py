from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('event/<str:pk>/', views.event, name="event"),
]