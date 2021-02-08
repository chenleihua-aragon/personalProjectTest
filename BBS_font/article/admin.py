from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Comments)
admin.site.register(Heat)


class Article_Manager(admin.ModelAdmin):
    list_display = ["title", "article_type", "introduce"]

admin.site.register(Article, Article_Manager)