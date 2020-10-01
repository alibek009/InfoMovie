from django.db import models

# Create your models here.

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length= 150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

