from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate , login as handle_login


def index(req):
    return render(req,"index.html")

def home(req):
    return render(req,"home.html")

def login(req):
    try:
        if(req.method=='GET'):
            return render(req , 'index.html')
        elif(req.method=='POST'):
            user = authenticate(req , username = req.POST.get('username') , password=req.POST.get('password'))
            print(user)
            if user is not None :
                handle_login(req , user)
                return redirect('home')
            else:
                raise Exception("Invalid credentials")
    except Exception as e :
        print(str(e))
        return render(req , 'index.html')

def register(req):
    if(req.method=="POST"):
        try:
            user = User()
            user.first_name = req.POST.get("first_name")
            user.last_name = req.POST.get("last_name")
            user.email = req.POST.get("email")
            user.username = req.POST.get("user_name")
            user.set_password(req.POST.get("password"))
            user.is_active = True
            user.is_staff = True

            user.save()
            
            r = req.POST
            account = Account()
            account.user = user 
            account.dob = r.get('dob')
            account.gender = r.get('gender')
            account.contact = r.get('contact')

            account.save()
            return render(req,"index.html")

        except Exception as e:
            return render(req , "index.html")
    

