# Generated by Django 4.2.1 on 2024-02-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='link_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]
