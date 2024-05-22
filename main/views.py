from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

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

def login_user(response):
    return render(response, 'main/login.html', {})

def signup(response):
    return render(response, 'main/signup.html', {})


def addBook(response):
    return render(response, 'main/addBook.html', {})

def saveNewBook(request):
    if request.method == 'POST':
        name = request.POST['bookName']
        author = request.POST['author']
        category = request.POST['category']
        numberOfPages = request.POST['no_of_pages']
        description = request.POST['description']
        rating = request.POST['rating']
        
        bookCover = None
        if 'upImg' in request.FILES:
            bookCover = request.FILES['upImg']

        new_book = Book(
            name=name,
            author=author,
            category=category,
            numberOfPages=numberOfPages,
            description=description,
            rating=rating,
            bookCover=bookCover,
            isBorrowed=False  
        )
        new_book.save()
        return redirect('allBooks')  
    else:
        return redirect('addBook')


def editBook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'main/editBook.html', {'book': book})

def updateBook(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        book.name = request.POST['name']
        book.author = request.POST['author']
        book.numberOfPages = request.POST['numberOfPages']
        book.category = request.POST['category']
        book.description = request.POST['description']
        book.rating = request.POST['rating']
        
        if 'bookCover' in request.FILES:
            book.bookCover = request.FILES['bookCover']

        book.save()
        return redirect('bookDetails', book_id=book.id)
    else:
        return redirect('editBook', book_id=book_id)

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('allBooks')  
    else:
        return redirect('bookDetails', book_id=book_id)

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
        
        try:
            user = User.objects.create(
                username=username,
                password=make_password(password),
                email=email,
                is_staff=is_admin
            )
            user.save()
            user = authenticate(request, username=username, password=password, email=email)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=400)

    return JsonResponse({'status' : 'fail', 'error': 'Invalid request method'}, status=400)