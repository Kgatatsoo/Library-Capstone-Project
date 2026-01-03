from django.urls import path
from .views import helloView, addBookView, addBook

urlpatterns = [
    path('', helloView, name='home'),
    path("add-book/",addBookView),
    path("addbookdata/",addBook),

]
