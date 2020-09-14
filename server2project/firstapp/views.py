from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ImageClass, PatientClass
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
        # files= request.POST
        # context = {
        #     'files' : files
        # }
        print(request)
        fs= FileSystemStorage() #파일 저장관련 함수?
        # fileobj= request.FILES["filepath"] # request에 담아 온 파일을 fileobj에 저장, filepath는 xray.html에서 업로드할 이미지를 지정한 이름
        # filepathname= fs.save(fileobj.name, fileobj) # context에 담아 보내기 위해 파일을 다시 저장해준다
        # files= request.POST
        files= request.POST.get('src')
        print(files)
        context= {
            'files': files
        }
        return render(request,'xrayresult.html', context)

    return render(request, 'xrayresult.html', context)

def ctresult(request):
    return render(request, 'ctresult.html')

def mydata(request):
    return render(request, 'mydata.html')



ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST': '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING': '아이디와 비밀번호를 확인해주세요.',
    'PW_CHECK': '비밀번호가 일치하지 않습니다.'
}


def signup(request):    # url에서 정보를 받아온다

    context= {
        'error':{
            'state': False,
            'msg':''
        }
    }

    if request.method == "POST":    # signup.html에서 버튼을 누르면 post가 온다

        # post에 담긴 내용들
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']
        name = request.POST['name']
        age= request.POST['age']
        email = request.POST['email']
        phone_num = request.POST['phone_num']

        if (user_id and user_pw): #아이디 비번 있는 경우??
            user= User.objects.filter(username=user_id)
            # user= User.objects.all()
            if len(user)==0:

                if user_pw == user_pw_check:

                    # participate_image= ImageClass.objects.get(imagename=imagename)

                    created_user = User.objects.create_user(
                        username= user_id,
                        password= user_pw
                    )

                    #추가
                    PatientClass.objects.create(
                        # participate_image=participate_image,
                        user= created_user,
                        name= name,
                        age= age,
                        phone_num= phone_num
                    )

                    auth.login(request, created_user)

                    return redirect('main') # 버튼을 눌러서 post가 갔다가 if에 만족하니 다시 main으로 돌아간다
                    # context = {
                    #     'user': user
                    # }

                    # return render(request, 'main.html', context)

                else:   # 비번과 비번 재입력값이 다른 경우
                    context['error']['state']=True
                    context['error']['msg']= ERROR_MSG['PW_CHECK']

            else:   # 아이디가 존재하는 경우
                context['error']['state']=True
                context['error']['msg']= ERROR_MSG['ID_EXIST']
        
        else:   # 아이디 비번 없는 경우
            context['error']['state']=True
            context['error']['msg']= ERROR_MSG['ID_PW_MISSING']

    return render(request, 'signup.html', context) # html로 간다




def login(request):

    if request.method == "POST":
        return redirect('main')

    return render(request, 'login.html')


def uploadimage(request):
    print(request)
    fs= FileSystemStorage() #파일 저장관련 함수?
    fileobj= request.FILES["filepath"] # request에 담아 온 파일을 fileobj에 저장, filepath는 xray.html에서 업로드할 이미지를 지정한 이름
    filepathname= fs.save(fileobj.name, fileobj) # context에 담아 보내기 위해 파일을 다시 저장해준다
    filepathname= fs.url(filepathname) # 같은 이미지가 반복되서 업로드되면 파일 이름이 파생되어 생긴다
                                        # 그래서 파일의 url을 하나로 지정하여 저장하는 것 같다. 맞는지는 모르겠다

    context={
        'filepathname': filepathname
    }

    return render(request, 'xray.html', context) # 저장된 파일을 context에 담아 xray.html로 보낸다