from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Genre(models.Model):
    name_genre = models.CharField(max_length=30, verbose_name='Название категории')
    #пробуем использовать slug
    # url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name_genre

    def get_absolute_url(self):
        return reverse('genre_list', kwargs={"pk": self.pk})


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    country = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='video_poster/')
    # genre = models.ManyToManyField(Genre, verbose_name="жанры")
    genre = models.ManyToManyField(Genre, blank=True, related_name='videos', verbose_name="жанры")
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)
    # пробуем использовать slug
    # url = models.SlugField(max_length=130, unique=True, default='777')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('video', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('video', kwargs={"pk": self.pk})
