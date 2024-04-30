from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField
# Create your models here.
class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Первое описание"
    )
    descriptions2 = models.TextField(
        verbose_name="Второе описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="about_image/",
        verbose_name="Фотография"
    )
    def __str__(self):
        return self.descriptions
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class News(models.Model):
    descriptions = models.TextField(
        verbose_name="Начало"
    )
    descriptions2 = models.TextField(
        verbose_name="Середина"
    )
    descriptions3 = models.TextField(
        verbose_name="Конец"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="about_image/",
        verbose_name="Фотография"
    )
    def __str__(self):
        return self.descriptions
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
    descriptions = models.TextField(verbose_name='Описание')
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

class SingleParts(models.Model):
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="image/",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    descriptions = RichTextField(
        verbose_name="Описание"
    )
    video = models.URLField(
        verbose_name="Видео"
    )

    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    class Meta:
        verbose_name_plural = "Одиночные детали"