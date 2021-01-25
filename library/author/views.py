from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from author.models import Author


def get_all_authors(request):
    author1 = Author(id=1, name="Victor", surname="Hugo")
    author1.save()
    author2 = Author(id=2, name="Honore", surname="Balzac")
    author2.save()
    author3 = Author(id=3, name="Jean", surname="Moliere")
    author3.save()

    context = {'authors_list': Author.objects.all()}
    return render(request, 'authors_list.html', context)


def get_by_id(request, id):
    author = Author.get_by_id(id)
    context = {'author': author}
    return render(request, 'author.html', context)


def delete_all_authors(request):
    authors = Author.objects.all()
    authors.delete()
    return redirect('authors_list')


def delete_author_by_id(request, id):
    context = {}
    obj = get_object_or_404(Author, pk=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("authors_list"))
    return render(request, "delete_author_by_id.html", context)


class AuthorList(ListView):
    model = Author
