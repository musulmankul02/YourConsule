# Generated by Django 5.0.4 on 2024-04-27 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_year_rename_decriptions_about_descriptions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория года',
                'verbose_name_plural': 'Категории года',
            },
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'История', 'verbose_name_plural': 'Истории'},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'verbose_name': 'Год', 'verbose_name_plural': 'Года'},
        ),
        migrations.RemoveField(
            model_name='history',
            name='years',
        ),
        migrations.RemoveField(
            model_name='year',
            name='years',
        ),
        migrations.AddField(
            model_name='history',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='history_items', to='secondary.year', verbose_name='Год'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='year',
            name='year',
            field=models.CharField(default=1, max_length=255, verbose_name='Год'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='descriptions',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.ImageField(upload_to='history_images/', verbose_name='Фотография'),
        ),
        migrations.AddField(
            model_name='year',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='years', to='secondary.category', verbose_name='Категория года'),
            preserve_default=False,
        ),
    ]