from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50)
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
    service = models.CharField(max_length=30)

    def __str__(self):
        return f'Service - {self.service}'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Price(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f'Service - {self.title} costs {self.price}'

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'