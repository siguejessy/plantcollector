from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plants_index, name='index'),
  path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
  path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
]