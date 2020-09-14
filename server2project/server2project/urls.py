"""server2project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),

    path('xray/', views.xray, name='xray'),
    path('ct/', views.ct, name='ct'),

    path('xray/result/', views.xrayresult, name='xrayresult'),
    path('ct/result/', views.ctresult, name='ctresult'),

    path('mydata', views.mydata, name='mydata'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

    url('uploadimage', views.uploadimage, name='uploadimage'), # xray.html에서 온 사진을 views에 있는 uploadimage로 보낸다
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)