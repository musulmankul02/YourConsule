from django.db import models

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