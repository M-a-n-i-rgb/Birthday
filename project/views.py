from django.shortcuts import render

# Create your views here.


def latern(request):
    return render (request,'project/latern.html')

def article1(request):
    return render (request,'project/article1.html')

def article2(request):
    return render (request,'project/article2.html')

def article3(request):
    return render(request,'project/article3.html')

def article4(request):
    return render(request,'project/article4.html')