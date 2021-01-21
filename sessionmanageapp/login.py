from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.views import  View
from django.contrib.sessions.models import Session
from .models import User

class Login(View):
    def get(self,request):
        user = request.session.get('user')
        print(user)
        if not user:
            return render(request,'login.html')
        else:
            email = request.session['email']
            user = User.get_user_by_email(email)
            data = {
                'firstname':user.first_name,
            }
        return redirect('homepage')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_user_by_email(email)
        error_message = None
        if user:
            flag = check_password(password,user.password)
            if flag:
                request.session['user'] = user.id
                request.session['email']=user.email
                return redirect('/')
            else:
                error_message = 'Invalid Email or Password !!!'
        else:
            error_message = 'Invalid Email or Password !!!'
        return render(request, 'login.html', {'error': error_message})

def Logout(request):
    request.session.clear()
    return redirect('login')
