from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    return render(request, 'main.html')

def xray(request):
    return render(request, 'xray.html')

def ct(request):
    return render(request, 'ct.html')

def xrayresult(request):
    return render(request, 'xrayresult.html')

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
        email = request.POST['email']
        phone_num = request.POST['phone_num']

        if (user_id and user_pw): #아이디 비번 있는 경우
            user= User.objects.filter(username=user_id)
            
            return redirect('main') # 버튼을 눌러서 post가 갔다가 if에 만족하니 다시 main으로 돌아간다
            
        
        else:   # 아이디 비번 없는 경우
            context['error']['state']=True
            context['error']['msg']= ERROR_MSG['ID_PW_MISSING']

    return render(request, 'signup.html', context) # html로 간다




def login(request):

    if request.method == "POST":
        return redirect('main')

    return render(request, 'login.html')