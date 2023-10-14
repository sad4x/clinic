from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import About, Guarantee, Service, Feature, Doctor, Testimonial, Appointment

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

def appointment(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        doc = request.POST.get('doctor')
        doctor = Doctor.objects.get(name=doc)
        date = request.POST.get('date')
        time = request.POST.get('time')
        problem = request.POST.get('problem')
        Appointment.objects.create(name=name,email=email,phone=phone,doctor=doctor,date=date,time=time,problem=problem)
        return redirect('/')

    return render(request,'appointment.html', {'doctors':Doctor.objects.all()})
def about(request):
    context = {
        'abouts':About.objects.all(),
        'guarantees':Guarantee.objects.all()
    }
    return render(request,'about.html',context)

def about_more(request):
    context = {
        'abouts':About.objects.all(),
        'guarantees':Guarantee.objects.all()
    }
    return render(request,'about_more.html',context)

def error(request):
    return render(request,'404.html')

def contact(request):
    if request.POST:

    return render(request,'contact.html')

def feature(request):
    context = {
        'features':Feature.objects.all()
    }
    return render(request,'feature.html',context)

def service(request):
    context = {
        'services':Service.objects.all()
    }
    return render(request,'service.html',context)

def team(request):
    context = {
        'doctors':Doctor.objects.all()
    }
    return render(request,'team.html',context)

def testimonial(request):
    context = {
        'testimonials':Testimonial.objects.all()
    }
    return render(request,'testimonial.html',context)