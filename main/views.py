from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import books

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def bookss(request):
    bib_books = books.objects.all()
    return render(request, 'books.html', {"books": bib_books})

def second(request):
    return HttpResponse('second page')

def add(request):
    return render(request, "ok.html")

def delite(request):
    return render(request, "del.html")

def change(request):
    return render(request, "change.html")