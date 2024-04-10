from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Ссылка')
    link_img = models.FileField(upload_to='uploads/', verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]

    def get_absolute_url(self):
        return reversed('articles', kwargs={"id": self.slug})
