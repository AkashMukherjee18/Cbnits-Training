from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage


from .forms import userForm
import os
import uuid
# {% load static %}
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
        print("-----name----",name)
        print("----eamil-----",email)
        print("----eamil-----",password)
        print("----eamil-----",repeatpassword)
        # return HttpResponse("okkk")
        return render(request, "login.html")

def login(request):
    return render(request, "login.html")

def design(request):
    return render(request,"design.html")

def form(request):
    return render(request,"form.html")

def Design1(request):
    return render(request,"Design1.html")

@csrf_exempt
def upload(request):
    # return HttpResponse("Success")
    return render(request, "Design1.html")

@csrf_exempt
def upload(request):
    desging_upload = request.POST.get("design_sess")
    if desging_upload == "design1":
        design_name = "Design1.html"
#     # elif desging_upload == "design2":
#     #     design_name = "Design2.html"
#     # elif desging_upload == "design3":
#     #     design_name = "Design3.html"
#     # elif desging_upload == "design4":
#     #     design_name = "Design4.html"
    if request.method == "POST":
        name = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        img= request.FILES['dp']
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
        
        
        key = uuid.uuid1()
        print(key,"---------------",img)
        # exit(0)
        # fss = FileSystemStorage()
        # file = fss.save(img.name, img)
        # print("===============",file)
        # file_url = fss.url(file)
        # img.save("{% static 'images/{img.filename}' %}")
        # img_new_name = "{% static '{key}{img.filename}' %}"
        # os.rename("{% static 'static/images/{img.filename}' %}","{% static 'static/images/{img_new_name}' %}")
        data={'dname': name, 'dlname': lastname, 'dsch': school, 'dcol': college, 'dimg': img, 'dph': phone, 'demail': email, 'ds1': skill1, 'ds2': skill2, 'ds3': skill3, 'ds4': skill4, 'dabout': about, 'git': git, 'insta':insta}
        return render(request, "Design1.html", data)
        # return render(request, 'Design1.html')
# def delete():
#     files = os.listdir("static/images")
#     for f in files:
#         os.remove(f"static/images/{f}")


def aboutUS(request):
    return HttpResponse("<b>Welcome to Wscubetech</b>")

def course(request):
    return HttpResponse("Welcome to Our Course")

def courseDetails(request, courseid):
    return HttpResponse(courseid+" Welcome to Our Course Details")
    # return HttpResponse(courseid)


