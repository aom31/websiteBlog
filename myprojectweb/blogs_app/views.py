from django.shortcuts import render
from django.http import HttpResponse
from category.models import CategoryBlog
# Create your views here.

def index(request):
    categories = CategoryBlog.objects.all()
    return render(request, "frontEnd/index.html", {'categories' : categories})