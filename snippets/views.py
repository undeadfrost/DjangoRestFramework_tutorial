from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer
# Create your views here.


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
