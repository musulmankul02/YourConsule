# Generated by Django 5.0.4 on 2024-04-27 10:39

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0006_team_alter_history_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.IntegerField(verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Катигория Года',
                'verbose_name_plural': 'Катигории Года',
            },
        ),
        migrations.RenameField(
            model_name='about',
            old_name='decriptions',
            new_name='descriptions',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='decriptions2',
            new_name='descriptions2',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='decriptions',
            new_name='descriptions',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='decriptions2',
            new_name='descriptions2',
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_image/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='history',
            name='descriptions',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='history_image/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_image/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='team_image/', verbose_name='Ваше фото'),
        ),
        migrations.AlterField(
            model_name='history',
            name='years',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondary.year', verbose_name='Год'),
        ),
    ]