# Generated by Django 4.2.1 on 2024-02-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link_map', models.CharField(max_length=255)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-time_created'],
                'indexes': [models.Index(fields=['-time_created'], name='main_map_time_cr_ac597b_idx')],
            },
        ),
    ]