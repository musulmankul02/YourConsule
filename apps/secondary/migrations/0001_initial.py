# Generated by Django 5.0.4 on 2024-04-24 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decriptions', models.TextField(verbose_name='Первое описание')),
                ('decriptions2', models.TextField(verbose_name='Второе описание')),
                ('image', models.ImageField(upload_to='about_image', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='AboutInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('descritions', models.TextField(verbose_name='описание')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_inline', to='secondary.about')),
            ],
            options={
                'unique_together': {('about', 'title')},
            },
        ),
    ]
