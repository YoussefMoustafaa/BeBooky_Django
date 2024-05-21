from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

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

def search_books(request):
    query = request.GET.get('search', '')
    books = []
    if query:
        books = Book.objects.filter( Q(name__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, 'main/search_books.html', {'books': books, 'query': query})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        is_admin = request.POST.get('isAdmin') == 'true'

        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_staff = is_admin
        user.save()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, ('Registration Successful!'))
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'fail', 'error': 'Authentication failed'}, status=400)
    # return redirect('home')
    return JsonResponse({'status' : 'fail', 'error': 'Invalid request method'}, status=400)