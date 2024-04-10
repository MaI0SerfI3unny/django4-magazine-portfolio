from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    requirements = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    conditions = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]