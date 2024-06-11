from django import forms
from .models import Product,Category,Brand
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ["productName","category","brand","unitPrice","unitsInStock","description","image"]

        labels = {

            'prodcutName' : 'Ürün İsmi',
            'category' : 'Kategori',
            'brand': 'Marka',
            'unitPrice': 'Fiyat',
            'unitsInStock': 'Stok Adeti',
            'description': 'Açıklama',
            'image': 'Görsel'


        }


        def clean(self):
            cleaned_data = super().clean()

            productName = cleaned_data.get('productName')
            category = cleaned_data.get('category')
            brand = cleaned_data.get('brand')
            unitPrice = cleaned_data.get('unitPrice')
            unitsInStock = cleaned_data.get('unitsInStock')
            description = cleaned_data.get('description')
            image = cleaned_data.get('image')

            if productName and len(productName) <=5:
                raise ValidationError("Lütfen 5 karakterden fazla değer giriniz.")
            if unitPrice and unitPrice <=0:
                raise ValidationError("Lütfen bir fiyat giriniz.")
            
            return cleaned_data
            
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = ["categoryName"]
        labels = {
            'categoryName': 'Kategori ismi'
        }

        def clean(self):
            cleaned_data = super().clean()

            categoryName = cleaned_data.get('categoryName')

            if categoryName and len(categoryName)<=2:
                raise ValidationError("Kategori ismi en az 3 karakter olabilir")
            
            return cleaned_data

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand

        fields = ["brandName"]
        labels = {
            'brandName': 'Marka ismi'
        }

        def clean(self):
            cleaned_data = super().clean()

            brandName = cleaned_data.get('brandName')

            if brandName and len(brandName)<=2:
                raise ValidationError("Marka ismi en az 3 karakter olabilir")
            
            return cleaned_data
