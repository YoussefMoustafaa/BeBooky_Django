from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contactUs, name='contact-us'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('bookDetails/<int:book_id>/', views.bookDetails, name='bookDetails'),
]