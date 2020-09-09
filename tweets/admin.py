from django.contrib import admin

# Register your models here.
from .models import Tweet, TweetLike

class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike

class TweetAdmin(admin.ModelAdmin):
    inlines =[TweetLikeAdmin]
    search_fields = ['user__username', 'user__email']
    list_display = ['__str__', 'user']
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)