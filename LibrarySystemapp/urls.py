from django.urls import path
from .views import helloView,addBookView

urlpatterns = [
    path('', helloView, name='home'),
    path("add-book/",addBookView)
]
