from django.contrib import admin
from .models import Article
# Register your models here.

# admin.site.register(Article)

@admin.register(Article)
class Articleadmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')