from django.db import models

# Create your models here.

class treatment(models.Model): # 진료 클래스
    disease= models.CharField(max_length=30) # 병명
    nurse= models.CharField(max_length=30) # 담당 간호사
    doctor= models.CharField(max_length=30) # 담당 의사
    patient_num= models.IntegerField() # 환자 번호

class patient(models.Model): # 환자 클래스
    patient_id= models.CharField(max_length=30) # 환자 id
    patient_num= models.IntegerField(default=False) # 환자 번호
    name= models.CharField(max_length=30) # 환자 이름
    image= models.CharField(max_length=30, default=False) # 사진 종류
    phone_num= models.CharField(max_length=30) # 환자 핸드폰번호
    intro_text= models.TextField() # 환자 상세 정보
