from django.db import models
from blogs.models import Post, Product
from django.contrib import admin

# Register your models here.
admin.site.register(Post)


@admin.display(description='Harga')
def pricing(obj):
    return "${:.2f}".format(obj.price)


@admin.action(description='Hitung total price dari stock')
def action_total_price(modeladmin, request, queryset):
    for q in queryset:
        tp = q.price * q.stock
        q.total_price = tp
        q.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', pricing, 'stock', 'total_price', 'slug', 'owner',)
    # fields = ('title', 'slug'),
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('owner',)
    actions = [action_total_price]


