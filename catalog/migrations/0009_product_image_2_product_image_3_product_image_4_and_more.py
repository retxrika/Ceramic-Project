# Generated by Django 4.0.5 on 2022-07-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_compound_product_package_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/images', verbose_name='Изображение товара(Дополнительное)'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/images', verbose_name='Изображение товара(Дополнительное)'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/images', verbose_name='Изображение товара(Дополнительное)'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/images', verbose_name='Изображение товара(Дополнительное)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='compound',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='catalog/images', verbose_name='Изображение товара(Главное)'),
        ),
    ]
