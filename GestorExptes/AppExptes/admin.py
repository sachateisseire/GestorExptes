from django.contrib import admin
from .models import Avatar, Expediente, Personal, Sector

# Register your models here.

admin.site.register(Expediente)

admin.site.register(Personal)

admin.site.register(Sector)

admin.site.register(Avatar)