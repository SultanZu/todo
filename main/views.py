from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse('This is testing page!')

def second(request):
    return HttpResponse('second page')