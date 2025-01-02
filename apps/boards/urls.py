from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListCreateView.as_view(), name='board-list-create'),  # Empty path here
    path('<int:pk>/', views.BoardDetailView.as_view(), name='board-detail'),
    path('lists/', views.ListCreateView.as_view(), name='list-create'),
    path('cards/', views.CardCreateView.as_view(), name='card-create'),
]
