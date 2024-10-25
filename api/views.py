from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

# Create your views here.
@api_view(['GET', 'POST'])
def livros(request):
    if request.method == 'GET':
        livros = models.Livro.objects.all()
        serializer = serializers.LivroSerializer(livros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)