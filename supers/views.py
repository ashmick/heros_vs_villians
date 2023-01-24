from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Supers
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view (['GET', 'POST'])
def supers_list(request):
    if request.method== 'GET':
        super= Supers.object.all()
        serializer=SuperSerializer(super, many=True)
        return Response(serializer.data)
    
    elif request.method== 'POST':
        serializer=SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view (['GET', 'PUT', 'DELETE'])
def super_detail (request,pk):
    super=get_object_or_404(Supers, pk=pk)
    
    if request.method== 'GET':
        serialzer= SuperSerializer(super)
        return Response (serializer.data)
    
    elif request.method == 'PUT':
        serializer= SuperSerializer(super, data=request.data)
        serializer.is_valid (raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method== 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)