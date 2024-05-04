from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField
# Create your models here.


class News(models.Model):
    title = RichTextField(
        verbose_name="Название"
    )
    data = models.CharField(
        max_length=255,
        verbose_name="Дата"
    )
    descriptions = RichTextField(
        verbose_name=" Первое Описание"
    )
    descriptions2 = RichTextField(
        verbose_name="Второе Описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="about_image/",
        verbose_name="Фотография"
    )
    video = models.URLField(
        verbose_name="Видео"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Новости'

class Year(models.Model):
    title = models.CharField(max_length=255, verbose_name='Год')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'

class History(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, verbose_name='Год', related_name='history_items')
    title = models.CharField(max_length=255, verbose_name='Название')
    descriptions = RichTextField(verbose_name='Описание')
    image = models.ImageField(upload_to='history_images/', verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

class Team(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Профессия"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="team_image/",
        verbose_name="Ваше фото"
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp",
        blank=True,null=True
    )   
    instagram =models.URLField(
        verbose_name="instagram",
        blank=True,null=True
    )
    
    def __str__(self):
        return f"{self.title} - {self.work}"
    
    class Meta:
        verbose_name = "Наши юристы"
        verbose_name_plural = "Наш юрист"

class Legalinformation(models.Model):
    title = RichTextField(
        verbose_name="Название"
    )
    descriptions = RichTextField(
        verbose_name=" Первое Описание"
    )
    descriptions2 = RichTextField(
        verbose_name="Второе Описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="about_image/",
        verbose_name="Фотография"
    )
    image2 = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="about_image/",
        verbose_name="2 Фотография"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Юридическая информация'