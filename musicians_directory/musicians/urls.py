from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('musician/<int:pk>/', views.musician_detail, name='musician_detail'),
    path('musician/new/', views.musician_create, name='musician_create'),
    path('musician/<int:pk>/edit/', views.musician_edit, name='musician_edit'),
    path('musician/<int:pk>/delete/', views.musician_delete, name='musician_delete'),
]
