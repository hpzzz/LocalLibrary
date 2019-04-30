from django.contrib import admin

# Register your models here.
from catalog.models import Book, BookInstance, Author, Genre, Language
#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)


admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
    """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


#Add associated records at the same time (Book and BookInstance)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Register the admin classes for Book using the decorator
@admin.register(Book) # == admin.site.register()
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'display_language') #cant use genre becouse it is a ManyToManyField, django prevents it
    inlines = [BookInstanceInline]
# Register the admin classes for BookInstance using the decorator



