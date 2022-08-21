from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import os
import time

from django.views import View

def register(request):
    template_name='registration/register.html'
    return render (request, template_name)

# django auth app login system

class Login(View):
    template_name = 'registration/login.html'
    def get(self, request):
        
        return render(request,self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

        
        