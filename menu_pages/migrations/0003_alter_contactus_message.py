# Generated by Django 5.0.1 on 2024-01-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_pages', '0002_alter_contactus_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(),
        ),
    ]