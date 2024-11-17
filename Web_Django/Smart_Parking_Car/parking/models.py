from django.db import models

class ParkingZone(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    num_of_slots = models.PositiveIntegerField(default=6)  # Cố định số lượng vị trí là 6
    vacant_slots = models.PositiveIntegerField(default=6)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Đảm bảo num_of_slots luôn là 6
        if self.num_of_slots != 6:
            self.num_of_slots = 6  # Đảm bảo số lượng vị trí luôn là 6

        # Đảm bảo vacant_slots không vượt quá num_of_slots
        if self.vacant_slots > self.num_of_slots:
            self.vacant_slots = self.num_of_slots  # Không cho vacant_slots vượt quá num_of_slots

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
