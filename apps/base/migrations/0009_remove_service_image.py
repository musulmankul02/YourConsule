# Generated by Django 5.0.4 on 2024-04-25 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_slide_remove_settings_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
