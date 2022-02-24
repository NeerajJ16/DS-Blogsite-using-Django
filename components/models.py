from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from unicodedata import category
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default='abc')
    image = models.ImageField(upload_to='uploads/images/',default='abc')
    
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=100,unique=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = HTMLField()
    
    def __str__(self):
        return self.title
    
    @staticmethod
    def getNotesbyId(category_id):
        if category_id:
            return Note.objects.filter(category=category_id)
        else:
            return Note.objects.all()