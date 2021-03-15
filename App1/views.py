from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import members,board_dicription,about_us,contact
from product.models import product

def home(request):
    about = about_us.objects.all()
    mypro = product.objects.all()
    member = members.objects.all()
    dis = board_dicription.objects.all()
    return render(request,'index.html',{"about":about,"mypro":mypro,"member":member,"dis":dis})

def about(request):
    about=about_us.objects.all()
    dis = board_dicription.objects.all()
    member = members.objects.all()
    return render(request,'about.html', {"about":about,"member":member,"dis":dis})

def member(request):
    member=members.objects.all()
    dis=board_dicription.objects.all()
    return render(request, 'boardmembers.html', {"member":member,"dis":dis})



def contactus(request):
    return render(request,"contact.html")


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        Email = request.POST['Email']
        message = request.POST['message']
        subjects = request.POST['subjects']

        rakib = contact(name=name, Email=Email, message=message, subjects=subjects)
        rakib.save()

        return render(request, "index.html")

    else:
        return render(request,'contact.html')

def mer(request):
    return render(request,'merchandising.html')



