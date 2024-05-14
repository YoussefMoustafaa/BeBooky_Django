from django.shortcuts import render, get_object_or_404
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


def bookDetails(response, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(response, 'main/bookDetails.html', {'book': book})
