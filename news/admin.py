from django.contrib import admin

# Register your models here.
from .models import News
from .models import Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', "created_at", 'update_at', "is_published")
    search_fields = ("title", "content")
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_filter = ("is_published",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', "news")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("id", "title")


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
