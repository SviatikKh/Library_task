from django.contrib import admin
from author.models import Author
from book.models import Book


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
