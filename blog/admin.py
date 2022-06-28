from atexit import register
from django.contrib import admin

from .models import Post
# Register your models here.

#Ahora vamos a registrar el modelo de POST que hemos creado:
admin.site.register(Post)