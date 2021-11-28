from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.TextField(primary_key=True)
    name = models.TextField()
    price = models.TextField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.TextField()
    slug = models.TextField()
    pass
