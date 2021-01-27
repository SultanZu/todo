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
    book = books(title=title,
        subtitle=subTitle,
        description=desc,
        genre=genre,
        author=author,
        year=year,
        price=price)
    book.save()
    return redirect(bookss)

def delete_book(request, id):
    book = books.objects.get(id=id)
    book.delete()
    return redirect(bookss)

def mark_book(request, id):
    book = books.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(bookss)

def unmark_book(request, id):
    book = books.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(bookss)

def book_details(request, id):
    bib_books = books.objects.filter(id=id)
    return render(request, 'books_detail.html', {"books": bib_books})

def book_back(request):
    return redirect(bookss)

def todo(request, id):
    todo_object = ToDo.objects.filter(id=id)
    return render(request, 'test.html', {"todo_list": todo_object})

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

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)