from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline', 'content', 'author', 'label', 'date_added')

admin.site.register(News, NewsAdmin)