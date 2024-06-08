from django.urls import path
from . import views

urlpatterns = [
    path('my-form/', views.my_form_view, name='my_form'),
]
