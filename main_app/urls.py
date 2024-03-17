from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plants_index, name='index'),
  path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
  path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
  path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
  path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
  path('plants/<int:plant_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('plants/<int:plant_id>/assoc_holder/<int:holder_id>/', views.assoc_holder, name='assoc_holder'),
  path('plants/<int:plant_id>/unassoc_holder/<int:holder_id>/', views.unassoc_holder, name='unassoc_holder'),
  path('holders/', views.HolderList.as_view(), name='holders_index'),
  path('holders/<int:pk>/', views.HolderDetail.as_view(), name='holders_detail'),
  path('holders/create/', views.HolderCreate.as_view(), name='holders_create'),
  path('holders/<int:pk>/update/', views.HolderUpdate.as_view(), name='holders_update'),
  path('holders/<int:pk>/delete/', views.HolderDelete.as_view(), name='holders_delete'),
]
