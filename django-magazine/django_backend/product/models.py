from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Ссылка')
    price = models.FloatField(max_length=255, default=0)
    discount = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    link_img = models.FileField(upload_to='product/', verbose_name='Фото')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Ссылка')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    link_img = models.FileField(upload_to='category/', verbose_name='Фото')

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug