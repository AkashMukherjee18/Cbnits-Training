# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
#from django.contrib.sessions import session
from .models import User, Login


# from .forms import userForm
import os
import uuid

# def home(request):
#     data={
#         'title': 'Home Page',
#         'bdata': 'Welcome to our page',
#         'clist': ['PHP', 'JAVA', 'Django'],
#         'numbers':[10,20,30,40,50,60,70,80],
#         # 'numbers':[],
#         'student_details':[
#             {'name': 'bikash', 'age': 24},
#             {'name': 'subash', 'age': 29}
#         ]
#     }
#     return render(request, "index.html",data)

def home1(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")


@csrf_exempt
def signupdata(request):
    # desging_upload = request.POST.get("signup.html")
    # if desging_upload == "signup":
    if request.method == "POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        password =request.POST.get("password")
        repeatpassword =request.POST.get("repeatpassword")
        new_user =User(name=name, email=email, password=password, repeatpassword=repeatpassword)
        new_user.save()
        return render(request, "login.html")
        # return render(request, "login.html")

def login(request):
    return render(request, "login.html")

@csrf_exempt
def logindata(request):
    if request.method == "POST":
        email= request.POST.get("email")
        password= request.POST.get("password")
        # print("------------------",password)
        field_email = 'email'
        field_password = 'password'
        try:
            obj = User.objects.get(email = email)
            field_email_value = getattr(obj, field_email)
            field_password_value = getattr(obj, field_password)
            if email == field_email_value and field_password_value == password:
                login_user =Login(email = field_email_value, password = field_password_value, user_id = obj)
                login_user.save()
                return render(request, "design.html")
            else:
                return HttpResponse("Please enter correct Password")
        except User.DoesNotExist:
            return HttpResponse("Please enter correct Email and Password Again")


            
def design(request):
    return render(request,"design.html")

# def form(request):
#     return render(request,"form.html")

def Design1(request):
    return render(request,"Design1.html")

def form(request, design):
    request.session["design_sess"] = str(design)+".html"
    print("-----------",design)
    return render(request, "form.html")

@csrf_exempt
def upload(request):
    desging_name = request.session['design_sess']
    if request.method == "POST":
        name = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        # img= request.FILES['dp']
        school = request.POST.get("school")
        college = request.POST.get("college")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        skill1 = request.POST.get("skill1")
        skill2 = request.POST.get("skill2") 
        skill3 = request.POST.get("skill3")
        skill4 = request.POST.get("skill4")
        about = request.POST.get("about")
        insta = request.POST.get("instagram")
        git = request.POST.get("github")
        
        
        # key = uuid.uuid1()
        in_memory_file_obj = request.FILES['dp']
        # print("-----------",in_memory_file_obj)
        img_new_name=FileSystemStorage(location="static/images/").save(in_memory_file_obj.name, in_memory_file_obj)
        data={'dname': name, 'dlname': lastname, 'dsch': school, 'dcol': college, 'dimg': img_new_name, 'dph': phone, 'demail': email, 'ds1': skill1, 'ds2': skill2, 'ds3': skill3, 'ds4': skill4, 'dabout': about, 'git': git, 'insta':insta}
        return render(request, desging_name, data)
        # return render(request, 'Design1.html')


def aboutUS(request):
    return HttpResponse("<b>Welcome to Wscubetech</b>")

def course(request):
    return HttpResponse("Welcome to Our Course")

def courseDetails(request, courseid):
    return HttpResponse(courseid+" Welcome to Our Course Details")

def Design2(request):
    return render(request, "Design2.html")

def Design3(request):
    return render(request, "Design3.html")

def Design4(request):
    return render(request, "Design4.html")
