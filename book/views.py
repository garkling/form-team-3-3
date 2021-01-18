from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from .models import Book
from order.models import Order
from order.forms import FilterForm


def all_books(request):
    books = Book.get_all()
    context = {'books': books}
    return render(request, 'all_books.html', context)


def book_page(request, book_id):
    book = Book.get_by_id(book_id)
    current_user = request.user
    order_end = datetime.datetime.now()

    if request.method == 'POST':
        form = FilterForm(request.POST or None)
        if form.is_valid():
            term = int(form.cleaned_data.get('select'))
            new_order = Order.create(current_user, book, datetime.datetime.now() + datetime.timedelta(days=term))
            new_order.save()
            return redirect('user-orders', request.user.uuid)

        return HttpResponse('Something went wrong!')

    select = FilterForm()
    is_ordered = Order.get(book_id=book.id, user_id=current_user.id, end_at=None)
    if is_ordered:
        order_end = is_ordered.plated_end_at

    context = {
        'book': book,
        'form': select,
        'is_ordered': is_ordered,
        'order_end': order_end.timestamp() * 1000
    }
    return render(request, 'book_page.html', context)
