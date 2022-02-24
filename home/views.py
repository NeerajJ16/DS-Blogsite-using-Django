from django.shortcuts import render, redirect
from .models import Image
from .models import About
from components.models import Note
from django.db.models import Q
from django.views.generic import TemplateView, ListView
# Create your views here.

def home(request):
    img = Image.objects.all()
    context = {'img' : img}
    return render(request, 'home/home.html',context)

def search(request):
    query=request.GET['query']
    #allNotes = Note.objects.filter(title__icontains=query)
    allNotes = Note.objects.filter( Q(title__icontains=query) | Q(description__icontains=query)) 
    params={'allNotes':allNotes, 'query':query}
    return render(request, 'home/search_result.html', params)

def about(request):
    abouts = About.objects.all()
    data = {'abouts':abouts}
    return render(request,'home/about.html',data)
