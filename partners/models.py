from django.db import models
from django.db.models.fields.files import ImageField

class PartnersCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='Текст для ссылки (введите название категории на английском)')
    image = models.ImageField(upload_to='partners/images' ,verbose_name='Изображение категории', null=True)
    descriprion = models.TextField(verbose_name='Описание категории', null=True)

    def __str__(self):
        return self.name


class PartnersProduct(models.Model):
    category = models.ForeignKey(PartnersCategory, verbose_name='Категория', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='catalog/images', verbose_name='Изображение товара', null=True)
    title = models.CharField(max_length=250, verbose_name='Имя товара')
    file = models.FileField(verbose_name='Файл для партнеров')

    def __str__(self):
        return self.title
