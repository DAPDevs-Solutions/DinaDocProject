from django.db import models
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Сообщение {self.message} от пользователя {self.name}"

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return f'Category - {self.category}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ServiceBlock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)

    def __str__(self):
        return f'Service - {self.service}'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
