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
    path('editBook/', views.editBook, name='editBook'),
    path('allBooks/', views.allBooks, name='allBooks'),
    path('register/', views.register, name='register'),
]