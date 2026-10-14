from django.contrib import admin
from .models import Book, Genre, Author

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ("name",)} 


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"] 


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ["title", "get_genres", "get_authors", "slug", "pages_count", "edition_year", "age_limit", "isbn", "publisher", "image"]
    list_filter = ["genres", "authors", "age_limit"]
    list_editable = ["pages_count", "edition_year"]
    prepopulated_fields = {'slug': ("title",)}

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = "Жанры"

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_authors.short_description = "Авторы"
