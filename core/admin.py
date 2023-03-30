from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'content', 'author', 'label')

admin.site.register(News, NewsAdmin)