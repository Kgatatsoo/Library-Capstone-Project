
from django.shortcuts import render
from .models import Book

def helloView(request):
    return render(request, "viewbook.html") 


def addBookView(request):
    if request.method=="POST":
        t=request.POST["tittle"]
        p=request.POST["price"]

        book=Book()
        book.title=t
        book.price=p
        book.save()
        return HttpResponse('/add-book')

    return render(request, "addbook.html",) 

