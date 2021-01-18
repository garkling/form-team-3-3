from django.shortcuts import render

from .models import Author


def all_authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'all_authors.html', context)


def author_page(request, author_id):
    author = Author.objects.get(uuid=author_id)
    books = author.books.all()
    context = {'author': author, 'books': books}
    return render(request, 'author_page.html', context)
