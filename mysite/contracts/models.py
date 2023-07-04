from django.db import models
from cars.models import Car
from users.models import Person, Department

class Contract(models.Model):
    vin = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Person, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    price = models.IntegerField(null=False, help_text='USD')
    release_date = models.DateField(null=True, help_text='Format YYYY-MM-DD', default='')
    details = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'contracts'

    def __str__(self) -> str:
        return "%s, %s" %(self.vin, self.client)