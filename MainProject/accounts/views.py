from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,authenticate
# Create your views here.
class Register(View):
    def get(self,request):
        context = {
            'form':RegisterForm()
        }
        return render(request,'accounts/register.html',context)
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request,'accounts/register.html',{'form':form})

class Login(View):
    def get(self,request):
        context = {
            'form':LoginForm(request.POST)
        }
        return render(request,'accounts/login.html',context)
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            if authenticate(form.cleaned_data['username'],form.cleaned_data['password'])
            login()
            return redirect("register")
        else:
            return render(request,'accounts/login.html',{'form':form})