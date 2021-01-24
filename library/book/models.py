from django.db import models, DataError
from author.models import Author


class Book(models.Model):
    name = models.CharField(blank=True, max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return f'Id {self.id}: {self.name}'

    @staticmethod
    def create(name, authors=None):
        book = Book(name=name)
        try:
            book.save()
            if authors is not None:
                for author in authors:
                    book.authors.add(author)
            book.save()
            return book
        except DataError:
            pass

    @staticmethod
    def get_by_id(book_id):
        book = Book.objects.get(id=book_id)
        return book

    @staticmethod
    def delete_by_id(book_id):
        book = Book.objects.get(id=book_id)
        book.delete()
        return True

    def update(self, name=None):
        if name:
            self.name = name
        self.save()

    def add_authors(self, authors):
        for author in authors:
            self.authors.add(author)
        self.save()

    @staticmethod
    def get_all():
        return list(Book.objects.all())
