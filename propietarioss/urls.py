from django.contrib import admin
from django.urls import path
from .views import propietarioListCreateView, propietarioDetailView

urlpatterns = [
    path('propietario/', propietarioListCreateView.as_view()),
    path('propietario/<int:pk>/', propietarioDetailView.as_view()),
]
