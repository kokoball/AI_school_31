from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ImageClass(models.Model):
    imagename= models.CharField(max_length=10)
    doctor= models.CharField(max_length=10)

class PatientClass(models.Model):
    name= models.CharField(max_length=10)
    age= models.CharField(max_length=5)
    phone_num= models.CharField(max_length=10)
    infotext= models.TextField()

    participate_image= models.ForeignKey(
        ImageClass, on_delete=models.CASCADE, related_name='patient'
    )

    user= models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='patient', default=' '
    )


class Photo(models.Model):
    post = models.ForeignKey(PatientClass, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)