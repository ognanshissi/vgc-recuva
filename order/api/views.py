from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from order.models import Order

from .serializers import OrderSerializer


class OrderCreateListAPIView(generics.ListCreateAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    # def get(self, request, format=None):
    #     orders = Order.objects.all()
    #     serialize = OrderSerializer(orders, many=True)
    #     return Response(serialize.data)
    #
    # def post(self, request, format=None):
    #     serializer = OrderSerializer(data=request.POST)
    #     data = request.POST
    #     return Response(data)
