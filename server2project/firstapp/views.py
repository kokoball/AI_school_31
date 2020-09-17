from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import DoctorClass, PatientClass, Photo
from django.contrib import auth
from django.core.files.storage import FileSystemStorage  # 이미지 업로드 관련 함수

# from keras.models import load_model
# from keras.preprocessing import image
# import json



# Create your views here.
def main(request):
    return render(request, 'main.html')

def xray(request):
    return render(request, 'xray.html')

def ct(request):
    return render(request, 'ct.html')

def xrayresult(request):

    if request.method == "POST":

        # image= Photo.objects.all()
        image= request.FILES
        
        context ={
            'image': image
        }
        print('!!!!!!!!!!', context)
        return render(request,'xrayresult.html', context)

    return render(request, 'xrayresult.html', context)

def ctresult(request):
    return render(request, 'ctresult.html')

def mydata(request):
    user= request.user

    # fs= FileSystemStorage()
    all_image= Photo.objects.filter(post_id=user)
    # all_image_url = all_image['image']
    # print('!!!!', all_image)
    # all_image= request.FILES['all_image']
    # all_image= fs.url(all_image)

    context= {
        'all_image': all_image,
        # 'all_image_url':all_image_url
    }
    
    return render(request, 'mydata.html', context)


def uploadimage(request):

    # 1번 방법
    
    # fs= FileSystemStorage() #파일 저장관련 함수?
    # fileobj= request.FILES["filepath"] # request에 담아 온 파일을 fileobj에 저장, filepath는 xray.html에서 업로드할 이미지를 지정한 이름
    # filepathname= fs.save(fileobj.name, fileobj) # context에 담아 보내기 위해 파일을 다시 저장해준다
    # filepathname= fs.url(filepathname) # 같은 이미지가 반복되서 업로드되면 파일 이름이 파생되어 생긴다
    #                                     # 그래서 파일의 url을 하나로 지정하여 저장하는 것 같다. 맞는지는 모르겠다

    # context={
    #     'filepathname': filepathname
    # }

    # post= request.user
    # Photo.objects.create(
    #     image= fileobj,
    #     post= post
  
    # )
    
    # ----------------------------

    # 2번 방법
    
    user= request.user

    image= None
    if 'image' in request.FILES:
        image= request.FILES['image']

    post= Photo(post=user, image=image)
    post.save()

    context= {
        'post': post
    }

    return render(request, 'xray.html', context) # 저장된 파일을 context에 담아 xray.html로 보낸다


# ---------------------------


