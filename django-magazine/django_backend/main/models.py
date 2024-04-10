from django.db import models


class Map(models.Model):
    title = models.CharField(max_length=255)
    link_map = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Карты"
        verbose_name_plural = "Карты"
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]