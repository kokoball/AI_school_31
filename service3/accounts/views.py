from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from firstapp.models import DoctorClass, PatientClass, Photo

# Create your views here.

def signup(request):
    context= {}
    
    if request.method == 'POST':

        ####
        user_id= request.POST['username']
        user_pw= request.POST['password']
        user_pw_check= request.POST['password_check']
        #####

        user_name= request.POST['name']
        #user_age= request.POST['age']
        #user_phone_num= request.POST['phone_num']
        #user_info= request.POST['info_text']
        

        if (user_id and user_pw and user_pw == user_pw_check):



            new_user= User.objects.create_user(
                username=user_id,
                password=user_pw
            )

            PatientClass.objects.create(
                user= new_user,
                name= user_name,
                #age= user_age,
                #phone_num= user_phone_num,
                #infotext= user_info

            )


            auth.login(request, new_user)
            return redirect('main')
        else:
            context['error']= '아이디 비번 확인'    

    return render(request, "accounts/signup.html", context)

def login(request):
    context={}

    if request.method== 'POST':
        if request.POST['username'] and request.POST['password']:

            user= auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if user is not None:
                auth.login(request, user)
                return redirect('main')
            else:
                context['error']= '아이디와 비번 확인'
        else:
            context['error']='아이디 비번 입력'

    return render(request, "accounts/login.html", context)

def logout(request):
    if request.method== 'POST':
        auth.logout(request)
        return render(request, 'main.html')

    return render('main.html')