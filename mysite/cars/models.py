from django.db import models
from users import models as mdl


class Car(models.Model):
    vin = models.CharField(max_length=17, blank=False)
    licence_plate = models.CharField(max_length=7)   
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    fuel_type = [
        ('Diesel', 'Diesel'),
        ('Gasoline', 'Gasoline')
    ]
    fuel = models.CharField(max_length=10, choices=fuel_type, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'cars'

    def __str__(self) -> str:
        return self.vin