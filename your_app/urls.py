from django.urls import path

from . import views
from .api import DashboardStatsAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/dashboard/', DashboardStatsAPIView.as_view(), name='dashboard-api'),
]
