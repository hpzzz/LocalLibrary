from django.contrib import admin

# Register your models here.
from catalog.models import Book, BookInstance, Author, Genre
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)
