from django.shortcuts import render, HttpResponseRedirect

# Home
def home(request):
    return render(request, 'index.html')

# About
def about(request):
    return render(request, 'about.html')

# Service
def service(request):
    return render(request, 'service.html')

# Menu
def menu(request):
    return render(request, 'menu.html')