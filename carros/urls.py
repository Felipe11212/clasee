from django.urls import path
from .views import carroListCreateView, carroDetailView

urlpatterns = [
    path('carro/', carroListCreateView.as_view(), name='carro-list-create'),
    path('carro/<int:pk>/', carroDetailView.as_view(), name='carro-detail'),
]
