from django.urls import path, include
from . import views 

urlpatterns = [
    path('non-primitive-ds',views.contents,name='contents'),
    path('notes',views.notePost, name='notePost'),
    path('<str:title>',views.lesson,name='lesson'),    
]