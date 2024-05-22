from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    numberOfPages = models.IntegerField()
    bookCover = models.ImageField(null=True, upload_to='images/')
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


