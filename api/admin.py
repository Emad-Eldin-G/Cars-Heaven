from django.contrib import admin
from .models import Brand, Model, Image, Blog

# Register your models here.
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Image)
admin.site.register(Blog)
