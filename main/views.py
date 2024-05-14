from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(response):
    booksList = Book.objects.all()
    return render(response, 'main/home.html', {'booksList': booksList})


def contactUs(response):
    return render(response, 'main/contact-us.html', {})


def aboutUs(response):
    return render(response, 'main/about-us.html', {})
