# Generated by Django 4.2.1 on 2024-03-15 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciens', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-time_created'], 'verbose_name': 'Вакансии', 'verbose_name_plural': 'Вакансии'},
        ),
    ]