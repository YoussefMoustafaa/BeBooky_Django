from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contactUs, name='contact-us'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('bookDetails/<int:book_id>/', views.bookDetails, name='bookDetails'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('addBook/', views.addBook, name='addBook'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('addBook/save/', views.saveNewBook, name='saveNewBook'),
    path('editBook/<int:book_id>/', views.editBook, name='editBook'),
    path('editBook/<int:book_id>/update/', views.updateBook, name='updateBook'),
    path('deletebook/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('allBooks/', views.allBooks, name='allBooks'),
    path('search/', views.search_books, name='search_books'),
    path('register/', views.register, name='register'),
]