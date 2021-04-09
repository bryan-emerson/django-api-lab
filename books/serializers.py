from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Book

class BookSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = Book
    fields = ('id', 'title', 'author')