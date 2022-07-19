# Generated by Django 4.0.5 on 2022-07-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_category_add_in_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='compound',
            field=models.CharField(max_length=250, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='product',
            name='package',
            field=models.CharField(max_length=250, null=True, verbose_name='Упаковка товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_of_package',
            field=models.CharField(max_length=250, null=True, verbose_name='Размер упаковки товара'),
        ),
    ]
