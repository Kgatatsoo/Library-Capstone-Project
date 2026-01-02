
from django.shortcuts import render

def helloView(request):
    return render(request, "viewbook.html") 


def addBookView(request):
    return render(request, "addbook.html") 

