from django.db import models
from django.contrib.auth.models import User
from django.db.models import Case, Value, When


class Person(models.Model):
    GENDER_TYPES = [
        ('F', 'Kobieta'),
        ('M', 'Mężczyzna')
    ]
    company = models.BooleanField()
    company_name = models.CharField(max_length=100, blank=True, default='')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES, null=True)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self) -> str:
        return "%s %s" %(self.last_name, self.first_name)

    

class Department(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'departments'

    def __str__(self) -> str:
        return "%s, %s" %(self.name, self.location)