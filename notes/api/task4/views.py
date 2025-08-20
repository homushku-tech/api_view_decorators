from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.task4.models import Order, Product
from api.task4.serializers import OrderSerializers

@api_view(['POST'])
def create_orders(requests):
    serializer = OrderSerializers(data = requests.data)
    if serializer.is_valid():
            print(serializer.data.get('products'))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    