from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.image_create, name='image_create'),
    path('details/<int:pk>/<slug:slug>/', views.image_detail, name='image_detail'),
]
