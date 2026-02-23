from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,'testapp/first.html')

def display2(request):
    return render(request,'testapp/second.html')