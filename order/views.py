from django.shortcuts import render, redirect
import datetime

from .models import Order
from book.models import Book


def all_orders(request, user_uuid):
    current_user = request.user
    open_orders = Order.get_not_returned_books_for_user(current_user.id)
    closed_orders = Order.objects.filter(end_at__isnull=False, user_id=current_user.id)
    context = {
        'open_orders': open_orders,
        'closed_orders': closed_orders
    }
    return render(request, 'all_orders.html', context)


def end_order(request, order_id):
    order = Order.get_by_id(order_id)
    order.end_at = datetime.datetime.now()
    book = Book.objects.get(id=order.book_id)
    book.count += 1

    book.save()
    order.save()
    return redirect('main')
