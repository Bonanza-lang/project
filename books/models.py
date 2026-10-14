from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-слаг")

    class Meta:        
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length = 100, db_index = True)

    class Meta:        
        ordering = ('name',)
        verbose_name = 'Автор'
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name

class Book(models.Model):
    genres = models.ManyToManyField(Genre, related_name="books")
    authors = models.ManyToManyField(Author, related_name = "books")
    title = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length=120, unique=True, verbose_name="URL-слаг")
    description = models.TextField(blank = True)
    pages_count = models.IntegerField()
    edition_year = models.IntegerField()
    age_limit = models.SmallIntegerField()
    isbn = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 100, db_index = True)
    image = models.ImageField(upload_to="books/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


