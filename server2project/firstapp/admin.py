from django.contrib import admin
from .models import ImageClass, PatientClass
# Register your models here.

admin.site.register(ImageClass)
admin.site.register(PatientClass)