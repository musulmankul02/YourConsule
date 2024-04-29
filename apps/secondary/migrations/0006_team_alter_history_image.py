# Generated by Django 5.0.4 on 2024-04-25 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='ФИО')),
                ('work', models.CharField(max_length=255, verbose_name='Профессия')),
                ('image', models.ImageField(upload_to='team_image', verbose_name='Ваше фото')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='instagram')),
            ],
            options={
                'verbose_name': 'Наши юристы',
                'verbose_name_plural': 'Наш юрист',
            },
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.ImageField(upload_to='history_image/', verbose_name='Фотография'),
        ),
    ]