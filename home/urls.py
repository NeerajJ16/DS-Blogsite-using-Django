from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search, name='search_results'),
    path('about',views.about,name='about'),
]