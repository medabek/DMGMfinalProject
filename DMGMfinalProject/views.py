from django.shortcuts import render
from django.views.generic import CreateView


def home(request):
    return render(request, 'home_page.html')

def home_page(request):
    return render(request, 'home.html')

def home_view(request):
    return render(request, 'home_form.html')