from django.contrib import admin
from django.urls import path
from .login import Login,Logout
from .signup import Signup
from .index import index

urlpatterns = [    
    path('',index,name='homepage'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout,name='logout'),
    path('signup/',Signup.as_view(),name='signup'),
]