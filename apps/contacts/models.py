from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField
# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия", 
        blank=True, null=True
    )
    phone = models.IntegerField(
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = "Форма обратной связи"

class Service(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )
    descriptions = RichTextField(
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