from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import  View
from django.contrib.sessions.models import Session
from .models import User

def index(request):
    user = request.session.get('user')
    print(user)
    if not user:
        return render(request,'index.html')
    email = request.session['email']
    user = User.get_user_by_email(email)
    data = {
        'firstname':user.first_name,
    }
    return render(request,'index.html',data)