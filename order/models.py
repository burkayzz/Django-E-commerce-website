from django.db import models
from django.contrib.auth.models import User
from Catalog.models import Product

# Create your models here.







class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Cart for {self.user.username}"
    

class Adres(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=25,verbose_name="Adres Başlığı")
    name_lastname = models.CharField(max_length=50,verbose_name="İsim ve Soyisim")
    phoneNumber= models.CharField(max_length=10,verbose_name="Telefon Numarası")
    eposta = models.EmailField(unique=True,verbose_name="E-Posta")
    adres = models.TextField(max_length=264,verbose_name="Adres Bilgileri")

    def __str_(self):
        return self.title



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Catalog.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.productName
    




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    adres = models.TextField(max_length=512,verbose_name="Adres Bilgileri")
    title= models.TextField(max_length=55,verbose_name="Adres Başlığı",default="Varsayılan Başlık")
    name_lastname = models.CharField(max_length=255, default='Varsayılan Ad Soyad',verbose_name="İsim Soyisim")
    
    
    
    status_choices = (
        ('bekliyor', 'Bekliyor'),
        ('sipariş oluşturuldu', 'Sipariş Oluşturuldu'),
        ('iptal edildi', 'İptal Edildi')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='bekliyor')

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.product.productName
    
class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    status_choices = (
        ('kargoya verildi', 'Kargoya verildi'),
        ('dağıtıma çıktı', 'Dağıtıma çıktı'),
        ('Teslim edildi', 'Teslim edildi')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Kargoya verildi')

    def __str__(self):
        return str(self.order.id)
    

