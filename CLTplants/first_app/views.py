from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'first_app/index.html')
    #return HttpResponse("Hello, world.")

def shop(request):
    if request.method == "GET":
        return render(request, 'first_app/shop.html')

def shop(request):
    if request.method == "GET":
        return render(request, 'first_app/shop.html')

def contact(request):
    if request.method == "GET":
        return render(request, 'first_app/contact.html')

def apply(request):
    if request.method == "GET":
        return render(request, 'first_app/apply.html')
    