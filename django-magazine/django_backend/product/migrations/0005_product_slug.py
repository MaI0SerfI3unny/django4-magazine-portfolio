# Generated by Django 4.2.1 on 2024-03-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_options_category_link_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=True, max_length=255, unique=True, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]