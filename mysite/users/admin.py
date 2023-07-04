from django.contrib import admin
from users.models import Person, Department


admin.site.register(Person)
admin.site.register(Department)