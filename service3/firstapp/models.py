from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PatientClass(models.Model):
    name= models.CharField(max_length=10)
    age= models.CharField(max_length=5)
    phone_num= models.CharField(max_length=10)
    infotext= models.TextField()

    user= models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='mola'
    )


class Photo(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class DoctorClass(models.Model):
    imagename= models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)
    doctor= models.CharField(max_length=10)