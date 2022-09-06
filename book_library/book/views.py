from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from.models import Book
from django.urls import reverse_lazy

class BookListViews(ListView):
    template_name = 'book/book_list.html'
    model = Book

class BookDetailViews(DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class BookCreateViews(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title','text','category')
    success_url = reverse_lazy('book-list')

class BookDeleteViews(DeleteView):
    template_name = 'book/book_delete.html'
    model = Book
    success_url = reverse_lazy('book-list')

class BookUpdateViews(UpdateView):
    template_name= 'book/book_update.html'
    model = Book
    fields = ('title','text','category')
    success_url = reverse_lazy('book-list')