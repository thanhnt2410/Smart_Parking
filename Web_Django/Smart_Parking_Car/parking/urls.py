from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Trang chủ
    path('status/', views.parking_status, name='parking_status'),  # Trạng thái
]
