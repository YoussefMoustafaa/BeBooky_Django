from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
from BeBooky.settings import MEDIA_ROOT

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
    
    # def delete(self, *args, **kwargs):
    #     if self.bookCover:
    #         print(self.bookCover.name)
    #         file = self.bookCover.name.split('/')
    #         joinedFile = "\\".join(file)
    #         print(joinedFile)
    #         image_path = os.path.normpath(os.path.join(settings.MEDIA_ROOT, self.bookCover.name.lstrip('/')))

    #         if os.path.isfile(image_path):
    #             try:
    #                 os.remove(image_path)
    #                 # Debug: Confirm the file was deleted
    #                 print(f"Deleted image at path: {image_path}")
    #             except Exception as e:
    #                 # Debug: Print any error that occurs
    #                 print(f"Error deleting image at path: {image_path} - {e}")
    #         else:
    #             # Debug: If file does not exist
    #             print(f"File not found at path: {image_path}")

    #     super().delete(*args, **kwargs)


