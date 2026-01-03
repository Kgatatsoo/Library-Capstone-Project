
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book

def helloView(request):
    return render(request, "viewbook.html") 


def addBookView(request):
   
    return render(request, "addbook.html",) 

   # def addBook(request): 
     #  if request.method == "POST":
     #   t=request.POST["title"]
     #   p=request.POST["price"]

    #    print(t,p)
    #    book=Book()
     #   book.title=t
     #   book.price=p
     #   book.save()
      #  return HttpResponseRedirect('/')

def addBook(request):
    if request.method == "POST":
        t = request.POST["title"]
        p = request.POST["price"]

        book = Book()
        book.title = t
        book.price = p
        book.save()

        return HttpResponseRedirect('/')

