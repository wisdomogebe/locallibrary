from django.contrib import admin

# Register your models here.

from .models import Author, Book, BookInstance, Genre, Language

# Declaration of the BookInstanceInline class to enable us add BookInstance information inline to our Book detail.
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class BookInline(admin.TabularInline):
    model = Book

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', "date_of_death")]

    inlines = [BookInline]

# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

# Register the admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # Adding the BookInstance information inline to the Book detail
    inlines = [BookInstanceInline]

# Register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = ((None, {
        'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
        'fields': ('status', 'due_back', 'borrower')
    }),
    )