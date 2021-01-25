from rest_framework import serializers

from book.models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'cover']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'cover']
