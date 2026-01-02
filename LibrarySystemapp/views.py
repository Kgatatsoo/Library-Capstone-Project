
from django.shortcuts import render

def helloView(request):
    return render(request, "viewbook.html") 

