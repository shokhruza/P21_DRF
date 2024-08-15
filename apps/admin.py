from django.contrib import admin

from apps.models import Product, User, Category


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'discount', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
