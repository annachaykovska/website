from django.shortcuts import render

def home(request):
    return render(request, 'HomePage.html')

def login(request):
    return render(request, 'loginPage.html')


