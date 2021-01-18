from django.urls import path

from . import views

urlpatterns = [
    path('<user_uuid>/orders', views.all_orders, name='user-orders'),
    path('end/<order_id>', views.end_order, name='end_order')
]
