from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.views.generic import ListView

from author.models import Author
from book.models import Book

from .serializers import BookListSerializer, BookDetailSerializer
from rest_framework import generics


def get_all(request):
    books = Book.get_all()
    return render(request, 'get_all.html', context={'books': books})



def get_by_id(request, id):
    try:
        book = get_object_or_404(Book, id=id)
    except Http404:
        return render(request, 'book_404.html', {'id': id})
    else:
        authors = ', '.join([author.name for author in book.authors.all()])
        return render(request, 'get_by_id.html', context={'book': book, 'authors': authors})


def delete_by_id(request, id):
    try:
        get_object_or_404(Book, id=id)
    except Http404:
        return render(request, 'book_404.html', {'id': id})
    else:
        Book.delete_by_id(id)
        return redirect('book_get_all')


def clear_authors(request, id):
    book = Book.get_by_id(id)
    authors_list = [Author.get_by_id(authors.id) for authors in book.authors.all()]
    book.remove_authors(authors_list)
    return redirect('book_get_by_id', id)


class BookList(ListView):
    model = Book


# =====    REST   ============

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

