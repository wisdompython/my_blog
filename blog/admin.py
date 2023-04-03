from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import BlogPost, Category, Comment
admin.site.register(Category)
admin.site.register(Comment)
# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('scripts/tinyInject.js',)
