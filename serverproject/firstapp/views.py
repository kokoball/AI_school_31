from django.shortcuts import render, redirect
from .models import treatment, patient

# Create your views here.

def main(request):
# def main(request, treatment_pk):
    # print(treatment_pk)

    treatment_object= treatment.objects.all()
    # treatment_obj= treatment.objects.get(pk=treatment_pk)
    # patient_obj= patient.objects.filter(patient_num=treatment_pk

    context = {
        'treatment_object': treatment_object,
        # 'treatment_pk': treatment_pk,
        # 'treatment_obj': treatment_obj,
        # 'patient_obj': patient_obj
    }
        
    return render(request, 'main.html', context)

def upload(request, treatment_pk):
    print(treatment_pk)

    treatment_obj= treatment.objects.get(pk=treatment_pk)
    patient_obj= patient.objects.filter(patient_num=treatment_pk)

    context = {
        'treatment_pk': treatment_pk,
        'treatment_obj': treatment_obj,
        'patient_obj': patient_obj 
    }

    return render(request, 'upload.html', context)


def add(request, treatment_pk):
    treatment_obj= treatment.objects.get(pk=treatment_pk)

    if request.method=='POST':
        patient.objects.create(
            patient_num= treatment_pk,
            name= request.POST['name'],
            phone_num= request.POST['phone_num'],
            intro_text= request.POST['intro_text']
        )
        return redirect('upload', treatment_pk)
    
    context= {
        'treatment_obj': treatment_obj
    }
    return render(request, 'add.html', context)


ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디입니다',
    'ID_NOT_EXIST': '존재하지 않는 아이디입니다',
    'ID_PW_MISSING': '아이디와 비밀번호를 확인하세요',
    'PW_CHECK': '비밀번호가 일치하지 않습니다'
}

def signup(request):
    context= {
        'error': {
            'state': False,
            'msg': ''
        },
    }

    if requeset.method == 'POST':

        user_id= request.POST['user_id']
        user_pw= request.POST['user_pw']
        user_pw_check= request.POST['user_pw_check']

        user= User.objects.filter(username=user_id)

        if (user_id and user_pw): # 존재하지 않는 아이디일경우
            if len(user) == 0: # 등록된 유저가 없는 경우
                if (user_pw == user_pw_check):

                    user= User.objects.create_user(
                        username= user_id,
                        password= user_pw
                    )
                    auth.login(request, user)

                    return redirect('main')

            else: # 등록된 유저가 있는 경우
                context['error']['state']= True
                context['error']['msg']= ERROR_MSG['ID_EXIST']
        else: #아이디가 존재할 경우
            context['error']['state']= True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'sigup.html', context)

def login(request):

    context= {
        'error': {
            'state': False,
            'msg': ""
        },
    }

    if request.method=='POST':
        user_id= request.POST['user_id']
        user_pw= request.POST['user_pw']

        user= User.objects.filter(username= user_id)

        if (user_id and user_pw): #아이디가 없을 경우
            if len(user) !=0: #아이디가 잇을 경우

                user = auth.authenticate(
                    username= user_id,
                    password= user_pw
                )
                
                if user != None: # 아이디와 비번이 맞을때
                    auth.login(request, user)
                    return redirect('main')
                
                else: # 비번이 틀린경우
                    context['error']['state']= True
                    context['error']['msg']= ERROR_MSG['PW_CHECK']

            else: #아이디가 없을 경우
                context['error']['state'] =True
                context['error']['msg']= ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
    
    return render(request, 'login.html', context)

def logout(request):
    if request.method == "POST":
        auth.lognout(request)
    
    return redirect("main")