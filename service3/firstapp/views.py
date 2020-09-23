from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import DoctorClass, PatientClass, Photo
from django.contrib import auth
from django.core.files.storage import FileSystemStorage  # 이미지 업로드 관련 함수

# Create your views here.
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
import cv2
import numpy as np

from skimage.segmentation import mark_boundaries
import lime
from lime import lime_image

model= load_model('./models/covid_model.h5')
ct_model= load_model('./models/M3_E_300_ImageNet.h5')
ct_model2= load_model('./models/COV_dense_v2.h5')



def main(request):
    return render(request, 'main.html')

def xray(request):
    
    if request.method == "GET":
        return render(request, 'xray.html')

    return render(request, 'xray.html')

def ct(request):
    return render(request, 'ct.html')

def xrayresult(request, post_pk):


    if request.method == "POST":

        image= Photo.objects.get(pk=post_pk)

        image_url= image.image
        
        image_path= "./media/"+str(image_url)
        # print(image_path)


        test_image = cv2.imread(image_path)
        test_image = cv2.resize(test_image, (224,224),interpolation=cv2.INTER_NEAREST)
        test_image = np.expand_dims(test_image,axis=0)
        probs = model.predict(test_image)
        pred_class = np.argmax(probs)

        class_dict = {0:'COVID19',
              1:'NORMAL',
              2:'PNEUMONIA'}

        pred_class= class_dict[pred_class]


        context ={
            'image': image,
            'pred_class': pred_class,

        }
        
        return render(request,'xrayresult.html', context)

    return render(request, 'xrayresult.html')

def ctresult(request):
    return render(request, 'ctresult.html')

def mydata(request):
    user= request.user

    # fs= FileSystemStorage()
    all_image= Photo.objects.filter(post_id=user)
    # all_image_url = all_image['image']
    # print('!!!!', all_image)
    # all_image_url= request.FILES['all_image']
    # all_image= fs.url(all_image)

    context= {
        'all_image': all_image,
        # 'all_image_url':all_image_url
    }
    
    return render(request, 'mydata.html', context)


def uploadimage(request):

    # 2번 방법
    if request.method=="POST":
        user= request.user

        image= None
        if 'image' in request.FILES:
            image= request.FILES['image']

        post= Photo(post=user, image=image)
        post.save()
        
        pk= post.pk


        context= {
            'post': post,
            'pk': pk
            
        }

    return render(request, 'xray.html', context) # 저장된 파일을 context에 담아 xray.html로 보낸다


def imageshow(request, photo_id):
    image= Photo.objects.get(id=photo_id)
    photo_id= photo_id

    context= {
        'image': image,
        'photo_id': photo_id
    }

    return render(request, 'xrayresult.html', context)