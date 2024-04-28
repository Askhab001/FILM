from django.core.validators import FileExtensionValidator
from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=100)


class user(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    text = models.TextField('TEXT')
    publication_date = models.DateField('DATE')

    def __str__(self):
        return self.title


def as_views(views):
    return None


class Trainig(models.Model):
    date_of_publication = models.DateTimeField('date publications')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    category = models.CharField('category', max_length=100)
    Trainig_title = models.CharField('Заголовок', max_length=255)
    summary_training = models.CharField('Краткое Содержания', max_length=255)
    full_training = models.TextField('full text', blank=True)
    links_training = models.URLField('URL', blank=True)
    video_training = models.FileField('Видео', upload_to='video/',
                                      validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
                                      blank=True, )
    graphic_illustrations = models.ImageField('Иллюстрация’, upload_to = main/', blank=True, null=True)

    class Meta:
        verbose_name = 'Обучение'

    verbose_name_plural = 'Обучения'

class Meta:
    verbose_name = 'Обучение'
    verbose_name_plural = 'Обучения'


def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)
    self.training_title = None


def str(self):
    return self.training_title


def test_training_title(self):
    self.assertEqual(str(self.training), 'Test Training')


class Things(models.Model):
    title = models.CharField(max_length=100)


class CarBrandView(models.Model):
    title = models.CharField(max_length=100)

class ThingsSerializer(models.Model):
    title = models.CharField(max_length=100)


