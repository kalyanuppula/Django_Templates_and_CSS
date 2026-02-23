from django.shortcuts import render

# Create your views here.
def display1(request):
    return render(request,'testapp/first.html')
def display2(request):
    return render(request,'testapp/second.html')
def display3(request):
    return render(request,'testapp/third.html')
