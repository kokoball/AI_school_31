from django.contrib import admin
from .models import ImageClass, PatientClass, Photo
# Register your models here.

admin.site.register(ImageClass)
admin.site.register(PatientClass)
admin.site.register(Photo)