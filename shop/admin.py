from django.contrib import admin
from django.utils.html import format_html
from .models import Product, LatestNews, ContactMessage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('thumbnail', 'name', 'price', 'category')
	search_fields = ('name',)
	list_filter = ('category',)

	def thumbnail(self, obj):
		if obj.image:
			return format_html('<img src="{}" style="width:48px;height:48px;object-fit:cover;" />', obj.image.url)
		return '-'

	thumbnail.short_description = 'Image'


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'is_active', 'created_at', 'modified_at')
	list_filter = ('is_active', 'created_at')
	search_fields = ('title',)
	readonly_fields = ('created_at', 'modified_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')