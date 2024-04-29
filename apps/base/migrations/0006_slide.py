# Generated by Django 5.0.4 on 2024-04-24 16:06

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_review_image_alter_review_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='slider/image/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': '2) Настройка Слайда',
                'verbose_name_plural': '2) Настройки Слайдов',
            },
        ),
    ]
