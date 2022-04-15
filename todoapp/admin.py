from django.contrib import admin
from .models import todolist
# Register your models here.

@admin.register(todolist)
# admin.site.register(todolist)
class AdminProfile(admin.ModelAdmin):
    list_display = ['item_title', 'description',
                    'item_price', 'date']
    list_display_links = ['item_title']
    # list_editable = ('item_title',)
    list_filter = ['date']
    search_fields = ['item_title', 'item_price']