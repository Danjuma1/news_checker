from django.contrib import admin

from .models import UserProfile, User

class UserProfileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    # list_display = ('username', 'email', 'age_range')

admin.site.register(UserProfile)
