from django.contrib import admin
from blog.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["telephone", "first_name", "name", "price", "id", "slug"]
    prepopulated_fields = {"slug": ('name', 'area', 'price'), }


@admin.register(ElPartition)
class ElPartitionAdmin(admin.ModelAdmin):
    list_display = ["name", 'partition', "price", "slug"]
    prepopulated_fields = {"slug": ('name', 'partition'), }


@admin.register(Partition)
class PartitionAdmin(admin.ModelAdmin):
    list_display = ["name", "slug",]
    prepopulated_fields = {"slug": ('name', ), }


admin.site.register(Benefits)
admin.site.register(Benefit)
