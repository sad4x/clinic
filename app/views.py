from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import About, Guarantee, Service, Feature, Doctor, Testimonial

def main(request):
    context = {
        'abouts':About.objects.all(),
        'guarantees':Guarantee.objects.all(),
        'services':Service.objects.all(),
        'features':Feature.objects.all(),
        'doctors':Doctor.objects.all(),
        'testimonials':Testimonial.objects.all(),
    }
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.POST:
            pass
        return render(request,'index.html',context)

def login_u(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user == None:
            return redirect('/login/')

        else:
            login(request,user)
            return redirect('/')

    return render(request,'login.html')

def logout_u(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username,email=email,password=password, is_staff=True)
        return redirect('/login/')

    return render(request,'register.html')