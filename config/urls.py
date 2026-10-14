from django.contrib import admin
from django.urls import path
from monitoring import views
urlpatterns = [path('admin/', admin.site.urls), path('', views.dashboard, name='dashboard'), path('api/health/', views.health), path('api/detections/', views.detections), path('api/scan/', views.run_scan), path('api/brand-profile/', views.brand_profile)]
