# Generated by Django 4.0.5 on 2022-07-18 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Текст для ссылки (введите название товара на английском)')),
                ('image', models.ImageField(null=True, upload_to='catalog/images', verbose_name='Изображение категории')),
            ],
        ),
        migrations.CreateModel(
            name='PartnersProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriprion', models.TextField(null=True, verbose_name='Описание категории')),
                ('image', models.ImageField(null=True, upload_to='catalog/images', verbose_name='Изображение товара')),
                ('title', models.CharField(max_length=250, verbose_name='Имя товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.partnerscategory', verbose_name='Категория')),
            ],
        ),
    ]
