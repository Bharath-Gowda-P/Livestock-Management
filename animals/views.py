from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from livestock import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import stock

# Create your views here.


def welcome(request):
    if request.method == "POST":
        email = request.POST['email']
        username  = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/')

        if password != cpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if email in [None, '']:
            messages.error(request, "Email is required")
            return redirect('signup')

        if username in [None, '']:
            messages.error(request, "Username is required")
            return redirect('signup')

        if password in [None, '']:
            messages.error(request, "Password is required")
            return redirect('signup')

        if cpassword in [None, '']:
            messages.error(request, "Password Confirmation is required")
            return redirect('signup')            

        newuser = User.objects.create_user(username, email, password)
        newuser.save()
        
        return redirect('login/')
    return render(request, "animals/welcome.html")


def signup(request):
    return render(request, "animals/signup.html")


def login_view(request):
    if request.method == "POST":
      user = request.POST['username']
      pas = request.POST['password']
      user = authenticate(request, username=user, password=pas)
      if user is not None:
          login(request, user)
          return redirect('/home')
      else:
          messages.error(request, "INVALID CREDENTIALS")
          return redirect('/login')
    return render(request, "animals/login.html")


@login_required(login_url='login')
def home(request):
    data = stock.objects.all()
    context = {"data": data}
    
    return render(request, "animals/home.html", context)


def add(request):
    if request.method == "POST":
        aid = request.POST['aid']
        aclass = request.POST['aclass']
        sex = request.POST['sex']
        weight = request.POST['weight']
        insurance = request.POST['insurance']
        vstatus = request.POST['vstatus']
        vdate = request.POST['vdate']
        ddate = request.POST['ddate']
        newstock = stock(id=aid, aclass=aclass, sex=sex, weight=weight, insurance=insurance, vacstatus=vstatus, vdate=vdate, ddate=ddate)
        newstock.save()
        return redirect('/home')
    return render(request, "animals/add.html")
    

def edit(request, id):
    obj = stock.objects.get(id=id)
    context = {"obj": obj}
    return render(request, "animals/edit.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')

def delete_view(request, id):
    obj = stock.objects.get(id=id)
    obj.delete()
    data = stock.objects.all()
    context = {"data": data}
    return redirect('/home', context)