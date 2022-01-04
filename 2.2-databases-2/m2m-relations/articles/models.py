from django.db import models


class Object(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Object, through='Relationship', related_name='scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Relationship(models.Model):

    id = models.IntegerField(primary_key=True)
    article_title = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Object, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')
