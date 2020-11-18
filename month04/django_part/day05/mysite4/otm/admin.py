from django.contrib import admin
from otm.models import Press, Book

# Register your models here.
class PressManager(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['id', 'name']

class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'press_id']
    list_filter = ['title']
    search_fields = ['id', 'title']

admin.site.register(Press, PressManager)
admin.site.register(Book, BookManager)