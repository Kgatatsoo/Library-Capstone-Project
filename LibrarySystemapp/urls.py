from django.urls import path
from .views import helloView, addBookView, addBook,editBook,editBookView

urlpatterns = [
    path('', helloView, name='home'),
    path("add-book/",addBookView),
    path("addbookdata/",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),

]
