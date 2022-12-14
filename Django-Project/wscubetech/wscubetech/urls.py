"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from wscubetech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path('home_1/', views.home1),
    path('signup/', views.signup), #new add
    path('signup/login', views.login), #new add
    
    path('home_1/design/', views.design, name='design'),
    path('form/design1', views.form, name='form'),
    path('home_1/design/upload', views.upload, name='upload'),
    # path('home_1/design/upload', views.upload, name='upload'), # correct code 
    path('home_1/signupdata/', views.signupdata, name='signupdata'), # correct code change for signup data 1/12/2022
    path('about-us/', views.aboutUS),
    path('course/', views.course),
    path('course/<courseid>', views.courseDetails),
]
