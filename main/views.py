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

def login(response):
    return render(response, 'main/login.html', {})

def signup(response):
    return render(response, 'main/signup.html', {})


def addBook(response):
    return render(response, 'main/addBook.html', {})


def editBook(response):
    return render(response, 'main/editBook.html', {})


def allBooks(response):
    booksList = Book.objects.all()
    return render(response, 'main/allBooks.html', {'booksList': booksList})
