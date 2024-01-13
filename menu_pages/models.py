from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField()
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f"Сообщение {self.message} от пользователя {self.email}"

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
