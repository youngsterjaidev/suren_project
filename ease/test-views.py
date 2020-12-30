from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from fs import open_fs
from fs.osfs import OSFS
from datetime import datetime, date

today = date.today()
time = datetime.now()

new_file = time.strftime('%H-%M-%S')

home = open_fs("~/log/")

# Create your views here.
def index(request):
    print_file = home.listdir("/")
    return render(request, 'ease/home.html', {'files': print_file})

def indexing(request):
    if not request.user.is_authenticated:
        return render(request, "ease/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "ease/home.html", context)


def save_file_name(request):
    file_name = request.POST['name']
    date_file = new_file + '.txt'
    home.writetext(date_file, file_name)
    return HttpResponse("Your Text is Inserted !")

def create_file(request):
    home_fs = home.open('loging.txt')
    l = home_fs.read()
    return HttpResponse(l)

def get_all_files(request):
    get_file = home.listdir("/")
    return HttpResponse(get_file)

def login(request):
    return render(request, 'ease/login.html')

def create_account(request):
    name = request.POST['name']
    enroll = request.POST['enroll']
    create_folder = home.makedir(enroll)
    user_file = str(new_file) + '.txt'
    create_folder.writetext(user_file, enroll)
    return HttpResponse('Account Created !')


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user1 = authenticate(request, username=username, password=password)
    if user1 is not None:
        login(request, user1)
        return HttpResponseRedirect(reverse("indexing"))
    else:
        return render(request, "ease/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
