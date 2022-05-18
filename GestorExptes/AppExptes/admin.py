from django.contrib import admin
from .models import Expediente, Personal, Sector

# Register your models here.

admin.site.register(Expediente)

admin.site.register(Personal)

admin.site.register(Sector)