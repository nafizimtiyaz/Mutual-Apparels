from django.shortcuts import render

def woven(request):
    return render(request,'woven.html')

def sweater(request):
    return render(request,"sweater.html")

def denim(request):
    return render(request,"denim.html")

def accessories(request):
    return render(request,"accessories.html")


def design(request):
    return render(request,"design.html")


def ancillary(request):
    return render(request,"ancillary.html")

def normalwash(request):
    return render(request,"normal-wash.html")

def pigmentwash(request):
    return render(request,"pigment-wash.html")

def bleachwash(request):
    return render(request,"bleach-essh.html")

def stonewash(request):
    return render(request,"stone-wash.html")

def acidwash(request):
    return render(request,"acid-wash.html")

def enzymewash(request):
    return render(request,"enzyme-wash.html")

def custicwash(request):
    return render(request,"custic-wash.html")

def garmentwash(request):
    return render(request,"garment-wash.html")

def whitening(request):
    return render(request,"whitening.html")
