from django.urls import path

from . import views

urlpatterns = [
    path('<user_uuid>/orders', views.all_orders, name='user-orders'),
    path('end/<order_id>', views.end_order, name='end_order'),


    path('crud/admin-order-list', views.order_list, name='admin-order-list'),
    path('crud/create-order', views.order_form, name='insert-order'),
    path('crud/update-order/<order_uuid>', views.order_form, name='update-order'),
    path('crud/delete-order/<order_uuid>', views.delete_order, name='delete-order')
]
