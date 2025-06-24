from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def get_item(request):
    item_obj = Item.objects.all()
    serializer = ItemSerializer(item_obj , many = True)
    return Response({'status' : 200 , 'payload' : serializer.data})
