# Generated by Django 5.0.4 on 2024-04-30 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_injury_legalinsights_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legalinsights',
            old_name='image1',
            new_name='image2',
        ),
    ]