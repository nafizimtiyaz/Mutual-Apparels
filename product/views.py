from django.shortcuts import render
from .models import product


def ourpro(request):
    mypro=product.objects.all()
    return render(request,'product.html',{"mypro":mypro})