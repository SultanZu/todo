from django.shortcuts import render, HttpResponse, redirect
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

def add_book(request):
    form = request.POST
    title = form['book-title']
    subTitle = form['book-subtitle']
    desc = form['book-des']
    genre = form['book-genre']
    author = form['book-author']
    year = form['book-year']
    price = form['book-price']
    bookTi = books(title=title,
        subtitle=subTitle,
        description=desc,
        genre=genre,
        author=author,
        year=year,
        price=price)
    bookTi.save()
    return redirect(bookss)

def second(request):
    return HttpResponse('second page')

def add(request):
    return render(request, "ok.html")

def delite(request):
    return render(request, "del.html")

def change(request):
    return render(request, "change.html")

def add_todo(request):
    form = request.POST
    text = form["todo-text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)