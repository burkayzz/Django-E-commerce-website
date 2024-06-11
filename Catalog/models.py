from django.db import models

# Create your models here.



class Category(models.Model):

    categoryName = models.CharField(max_length=20)
    def __str__(self):
        return self.categoryName
    


  
class Brand(models.Model):

    brandName = models.CharField(max_length=25)
    def __str__(self):
        return self.brandName
    


class Product(models.Model):

    productName = models.CharField(max_length=150,verbose_name="Ürün ismi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Kategori")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,verbose_name="Marka")
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Fiyat")
    unitsInStock = models.IntegerField(default=0,verbose_name="Stok Adeti")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='product_images/',verbose_name="Görsel")

    def __str__(self):
        return self.productName

        
