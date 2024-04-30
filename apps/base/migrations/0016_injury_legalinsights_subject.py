# Generated by Django 5.0.4 on 2024-04-30 11:27

import ckeditor.fields
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_service_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Первое описание')),
                ('descriptions2', models.TextField(verbose_name='Второе описание')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_image/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name_plural': 'Юридическое правосудие по травмам',
            },
        ),
        migrations.CreateModel(
            name='Legalinsights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/', verbose_name='Фото')),
                ('image1', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image1/', verbose_name='2 Фото')),
            ],
            options={
                'verbose_name_plural': 'Юридическая информация',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название темы')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Первое описание')),
                ('descriptions2', ckeditor.fields.RichTextField(verbose_name='Второе описание')),
            ],
            options={
                'verbose_name_plural': 'Название новой темы',
            },
        ),
    ]