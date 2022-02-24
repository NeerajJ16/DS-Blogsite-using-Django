from multiprocessing import context
from django.shortcuts import render
from .models import Category
from .models import Note

# Create your views here.
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error/error_404.html', data)


def contents(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'home/contents.html',context)

def notePost(request):
    notes = None
    categoryID = request.GET.get('category')
    if categoryID:
        notes = Note.getNotesbyId(categoryID)
    else:
        notes = Note.objects.all()
    data={}
    data['notes'] = notes
    return render(request,'home/notes.html',data)

def lesson(request, title):
    categories = Category.objects.all()
    lessons = Note.objects.filter(title=title)
    cont = {'lessons':lessons, 'categories':categories}
    return render(request, 'home/lesson.html',cont)

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error/error_404.html', data)    