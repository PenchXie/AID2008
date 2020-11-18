from django.contrib import admin
from bookstore.models import Book


# Register your models here.
# 模型管理器类
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'press', 'price', 'market_price']
    list_display_links = ['id', 'title', 'press']
    list_filter = ['press']
    search_fields = ['id', 'title']
    list_editable = ['market_price']


admin.site.register(Book, BookManager)
