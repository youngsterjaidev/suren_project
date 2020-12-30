from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

from fs import open_fs
from fs.osfs import OSFS
from datetime import datetime, date

today = date.today()
time = datetime.now()

new_file = time.strftime('%H-%M-%S')

home = open_fs("~/log/")

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "ease/login.html", {"message": None})
    else:
        print("/" + request.user.username)
        new_email = request.user.email.replace('@', '-')
        file_path = "~/log/" + new_email + "/"
        get_file = open_fs(file_path)
        print(get_file)
        print_file = home.listdir("/" + new_email)
        print(print_file)
        file_data_arr = []
        for file in print_file:
            print(file)
            open_file = get_file.open(file)
            file_data = open_file.read()
            print(file_data.split("#"))
            file_data_arr.append({
                "nameFile": file,
                "file_data": file_data.split("#")
            })


    context = {
        "user": request.user,
        "files": print_file,
        "fileDataArr": file_data_arr
        #"fileData": file_data
    }
    return render(request, "ease/home.html", context)

def create_account(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    new_email = email.replace('@', '-')
    User.objects.create_user(name, email, password)
    create_folder = home.makedir(new_email)
    user_file = str(new_file) + '.txt'
    create_folder.writetext(user_file,"Attendence")
    return HttpResponse('Account Created !')

def signup(request):
    return render(request, 'ease/signup.html')

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ease/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "ease/login.html", {"message": "Logged out."})

def create_subject_file(request):
    new_email = request.user.email.replace('@', '-')
    select_current_folder = open_fs("~/log/" + new_email)
    date_file = request.POST["subject"] + "-" + str(today) + ".txt"
    select_current_folder.writetext(date_file, "Attendence")
    return HttpResponseRedirect("rel/" + date_file)

def flights(request, file_name, file_path):
    print(file_name, file_path)
    context = {
        "fileName": file_name,
        "filePath": file_path
    }
    return render(request, 'ease/rel.html', context)

def link(request):
    return render(request, 'ease/rel.html')

def change_link(request):
    name = request.POST['name']
    enroll = request.POST['enroll']
    update_file = request.POST['file']
    new_file_path = request.POST['link']
    new_email = new_file_path.replace('@', '-')
    select_current_folder = open_fs("~/log/" + new_email)
    file_data = select_current_folder.open(update_file)
    new_data = file_data.read() + str("#")  + name
    select_current_folder.writetext(update_file, new_data)
    return HttpResponse(new_data)

