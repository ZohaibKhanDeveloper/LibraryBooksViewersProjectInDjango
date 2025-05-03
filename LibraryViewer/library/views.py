from django.shortcuts import render
from library.models import Books_details
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def books(request):
    books = {'books':Books_details.objects.all()}
    return render(request,'books.html',books)