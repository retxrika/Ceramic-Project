# Generated by Django 3.0 on 2021-08-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='image',
            field=models.ImageField(null=True, upload_to='catalog/images', verbose_name='Фото для партнеров'),
        ),
    ]
