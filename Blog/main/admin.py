from django.contrib import admin
from main.models import *
# Register your models here.

model_list = [Korisnik,Reputacija,Blog,Komentar]
admin.site.register(model_list)