from django.shortcuts import render, redirect

from .models import Author
from .forms import AuthorCreationForm
from authentication.views import check_superuser


def author_catalog(request):
    authors = Author.get_all()
    context = {'authors': authors}
    return render(request, 'author_catalog.html', context)


def author_page(request, author_id):
    author = Author.objects.get(uuid=author_id)
    books = author.books.all()
    context = {'author': author, 'books': books}
    return render(request, 'author_page.html', context)


# admin side
def author_list(request):
    if not check_superuser(request):
        return redirect('main')

    context = {'authors': Author.get_all()}
    return render(request, 'crud/author_list.html', context)


def author_form(request, author_uuid=0):
    if not check_superuser(request):
        return redirect('main')

    author = Author.get_by_id(author_uuid)
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('admin-author-list')
    else:
        form = AuthorCreationForm(instance=author)

    context = {'form': form}
    return render(request, 'crud/author_form.html', context)


def delete_author(request, author_uuid):
    Author.delete_by_id(author_uuid)
    return redirect('admin-author-list')
