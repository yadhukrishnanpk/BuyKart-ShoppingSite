from django.contrib import admin
from .models import Category,Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_by', 'is_sold', 'created_at')
    list_filter = ('is_sold', 'category', 'created_at')
    search_fields = ('name', 'description', 'created_by__username')
    list_editable = ('price', 'is_sold')
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_count')
    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = "Total Items"