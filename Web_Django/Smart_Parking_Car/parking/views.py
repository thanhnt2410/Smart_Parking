from django.shortcuts import render
from .models import ParkingZone

def index(request):
    return render(request, 'index.html')

def parking_status(request):
    return render(request, 'status.html')

def parking_zone_view(request):
    # Tạo danh sách giả lập khu vực đỗ xe
    all_parking_zones = [
        {'name': 'Parking Zone 1', 'address': 'Location 1', 'vacant_slots': 4, 'price': 10.00},
        {'name': 'Parking Zone 2', 'address': 'Location 2', 'vacant_slots': 3, 'price': 15.00},
        {'name': 'Parking Zone 3', 'address': 'Location 3', 'vacant_slots': 5, 'price': 12.00},
        {'name': 'Parking Zone 4', 'address': 'Location 4', 'vacant_slots': 6, 'price': 8.00},
        {'name': 'Parking Zone 5', 'address': 'Location 5', 'vacant_slots': 2, 'price': 20.00},
        {'name': 'Parking Zone 6', 'address': 'Location 6', 'vacant_slots': 1, 'price': 25.00}
    ]
    slots = range(1, 7)  # Tạo dãy số từ 1 đến 6
    return render(request, 'index.html', {'all_parking_zones': all_parking_zones, 'slots': slots})