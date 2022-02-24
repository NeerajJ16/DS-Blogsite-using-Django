from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Image(models.Model):
    images = models.ImageField(upload_to='uploads/images/')

    @staticmethod
    
    def get_all_images():
        return Image.objects.all()
    
class About(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='uploads/images')
    description = models.TextField()
    
    @staticmethod
    
    def getAll():
        return About.objects.all()
    