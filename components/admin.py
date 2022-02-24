from django.contrib import admin
from components.forms import NoteAdminForm
from .models import Category
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "category")

# Register your models here.

admin.site.register(Category)
admin.site.register(Note, NoteAdmin)