from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = RichTextField(
        verbose_name="Описание сайта"
    )
    logo = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to = "logo_image/",
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    instagram = models.URLField(
        verbose_name="Instagram url",
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name="facebook url",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="youtube url",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="whatsapp url",
        blank=True, null=True
    )
    def __str__(self):
        return f"{self.title} {self.descriptions}"
    
    class Meta:
        verbose_name_plural = "Настройки"

class Service(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )
    descriptions = models.TextField(
        max_length=255,
        verbose_name="Описание про нащих услуг"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural ="Услуга"

class Review(models.Model):
    message = RichTextField(
        verbose_name="Сообщение"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    profession = models.CharField(
        max_length=255,
        verbose_name="Ваша Профессия"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to = "image/",
        verbose_name="Фотография"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural ="Отзыв"

class Slide(models.Model):
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="image/",
        verbose_name="Фото для сайта"
    )
    image1 = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="image1/",
        verbose_name="2 Фото для сайта"
    ) 
    class Meta:
        verbose_name_plural = "Слайд"

class Numbers(models.Model):
    client = models.CharField(
        max_length=255,
        verbose_name="Довольные клиенты"
    )
    team = models.CharField(
        max_length=255,
        verbose_name="Опытные юристы и адвокаты"
    )
    experience = models.CharField(
        max_length=255,
        verbose_name="Многолетний опыт"
    )
    critical = models.CharField(
        max_length=255,
        verbose_name="Критические случаи успешно решены"
    )
    review = models.CharField(
        max_length=255,
        verbose_name="Положительных отзывов"
    )
    def __str__(self):
        return f"{self.client} - {self.team} - {self.review} - {self.critical} - {self.experience}"
    
    class Meta:
        verbose_name_plural = "Мы в числах"

class Injury(models.Model):
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
        verbose_name_plural = 'Юридическое правосудие по травмам'

class Subject(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название темы"
    )
    descriptions = RichTextField(
        verbose_name="Первое описание"
    )
    descriptions2 = RichTextField(
        verbose_name="Второе описание"
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Название новой темы"

class Legalinsights(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = RichTextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="image/",
        verbose_name="Фото"
    )
    image2 = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="image1/",
        verbose_name="2 Фото"
    ) 
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    class Meta:
        verbose_name_plural = "Юридическая информация"