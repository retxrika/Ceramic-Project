from django.contrib import admin
from django.db import models
from .models import Slider, NumberOrder, About

admin.site.register(Slider)
admin.site.register(NumberOrder)
admin.site.register(About)

