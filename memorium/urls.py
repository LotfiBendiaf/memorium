from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemoryListView.as_view(), name='gallery'),
    path('photo/<int:pk>/', views.MemoryDetailView.as_view(), name='memory'),
    path('photo/<int:pk>/edit/', views.MemoryUpdateView.as_view(), name='edit_memory'),
    path('photo/<int:pk>/delete/', views.MemoryDeleteView.as_view(), name='delete_memory'),
    path('photo/new/', views.MemoryCreateView.as_view(), name='new_memory'),
]