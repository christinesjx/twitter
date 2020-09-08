from django.contrib import admin

# Register your models here.
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']
    list_display = ['__str__', 'user']
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)