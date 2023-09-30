from django.shortcuts import render
from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import status
from .serializers import OrderSerializer
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework.views import APIView


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrdersSearchView(APIView):
    def post(self, request, *args, **kwargs):
        count = request.data.get('count')
        date_from = request.data.get('date_from')
        date_to = request.data.get('date_to')

        print("HERE: "+str(count)+" "+str(date_from)+" "+str(date_to))

        # Validate input parameters
        if not (1 <= count <= 20):
            return Response({'error': 'Invalid count value'}, status=status.HTTP_400_BAD_REQUEST)

        # Query the database based on the input parameters
        orders = Order.objects.filter(date_created__range=(date_from, date_to)).prefetch_related('orderItems')[:count]

        # Serialize the data
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
