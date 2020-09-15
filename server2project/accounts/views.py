from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from firstapp.models import ImageClass, PatientClass, Photo

# Create your views here.

def signup(request):
    context= {}
    
    if request.method == 'POST':

        ####
        user_id= request.POST['username']
        user_pw= request.POST['password']
        user_pw_check= request.POST['password_check']
        #####
        
        # if (request.POST['username'] and request.POST['password'] and request.POST['password'] == request.POST['password_check']):
        #     new_user= User.objects.create_user(
        #         username= request.POST['username'],
        #         password= request.POST['password'],
        #     )
        if (user_id and user_pw and user_pw == user_pw_check):

            #####
            # user= User.objects.filter(useranme=user_id)
            ####

            participate_image= ImageClass.objects.get(
                participate_image=participate_image)

            new_user= User.objects.create_user(
                username=user_id,
                password=user_pw
            )

            #####
            PatientClass.objects.create(
                user= new_user,
                # name= name,
                # phone_num= phone_num
            )
            #####

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