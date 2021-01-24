from django.db import models


class Author(models.Model):
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return f'Id {self.id}: {self.name}'

    @staticmethod
    def create(name, surname):
        author = Author(name=name, surname=surname)
        author.save()
        return author

    @staticmethod
    def get_by_id(author_id):
        user = Author.objects.get(id=author_id)
        return user

    @staticmethod
    def delete_by_id(author_id):
        author = Author.objects.get(id=author_id)
        author.delete()
        return True

    def update(self, name=None, surname=None):
        if name:
            self.name = name
        if surname:
            self.surname = surname
        from django.db import transaction
        with transaction.atomic():
            self.save()

