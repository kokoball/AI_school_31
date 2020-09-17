from django.contrib import admin
from .models import DoctorClass, PatientClass, Photo
# Register your models here.

admin.site.register(DoctorClass)
admin.site.register(PatientClass)
admin.site.register(Photo)