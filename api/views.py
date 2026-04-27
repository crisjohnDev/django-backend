from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET', 'POST'])
def items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        return Response(ItemSerializer(items, many=True).data)

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return Response({"message": "Deleted"})