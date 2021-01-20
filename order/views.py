from django.shortcuts import render, redirect
import datetime

from .forms import OrderCreationForm
from .models import Order
from book.models import Book
from authentication.views import check_superuser

from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

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


#/////////////////////////////////////////////
# admin side
def order_list(request):
    if not check_superuser(request):
        return redirect('main')

    context = {'orders': Order.get_all()}
    return render(request, 'crud/order_list.html', context)


def order_form(request, order_uuid=0):
    if not check_superuser(request):
        return redirect('main')

    order = Order.get_by_id(order_uuid)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin-order-list')
    else:
        form = OrderCreationForm(instance=order)

    context = {'form': form}
    return render(request, 'crud/order_form.html', context)


def delete_order(request, order_uuid):
    Order.delete_by_id(order_uuid)
    return redirect('admin-order-list')