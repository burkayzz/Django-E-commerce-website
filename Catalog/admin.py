from django.contrib import admin
from .models import Category,Brand,Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    
    search_fields=["categoryName"]


    class Meta:
        model = Category



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    search_fields=["brandName"]

    class Meta:
        model = Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields=["productName"]
    list_display = ["productName","category","brand","unitsInStock","unitPrice"]
    list_display_links = ["category","brand"]
    list_filter= ["category","brand"]
    

    class Meta:
        model = Product