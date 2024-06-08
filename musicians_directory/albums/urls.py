from django.urls import path
from . import views

urlpatterns = [
    path('musician/<int:musician_pk>/album/new/', views.album_create, name='album_create'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
]
