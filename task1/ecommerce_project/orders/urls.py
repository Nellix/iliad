from django.urls import path
from .views import OrderList, OrderDetail, OrderItemList

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('ordersItems/', OrderItemList.as_view(), name='order-item-list'),
]