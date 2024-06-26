# Generated by Django 5.0.4 on 2024-04-24 13:51

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_setting_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='descriptions',
            field=models.TextField(verbose_name='Описание сайта'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo_image/', verbose_name='Логотип'),
        ),
    ]
