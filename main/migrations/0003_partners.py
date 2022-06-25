# Generated by Django 3.0 on 2021-08-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_numberorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст для партнеров')),
                ('file', models.FileField(upload_to='', verbose_name='Файл для партеров')),
            ],
        ),
    ]
