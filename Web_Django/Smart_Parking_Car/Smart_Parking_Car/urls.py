from django.contrib import admin
from django.urls import path, include  # Chắc chắn bạn đã import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parking.urls')),  # Bao gồm URL của ứng dụng parking
]
