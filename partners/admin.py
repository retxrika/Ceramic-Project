from django.contrib import admin
from django.db import models
from .models import PartnersCategory, PartnersProduct

admin.site.register(PartnersCategory)
admin.site.register(PartnersProduct)

