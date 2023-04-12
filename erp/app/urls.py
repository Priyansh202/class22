from django.urls import path
from app import views
from .views import *

urlpatterns = [
    path('class/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
     path('class3/<int:pk>/', views.class_detail, name='class-detail11'),
]
