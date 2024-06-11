from django.shortcuts import render, redirect ,get_object_or_404,get_list_or_404
from .models import Cart, CartItem ,OrderItem, Order,Adres,Shipment
from Catalog.models import Product
from .forms import CartItem,AdresForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from decimal import Decimal


#Sepet
@login_required
@user_passes_test(lambda u: not u.is_superuser)
def view_cart(request):


    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cartitem_set.all()
    
    total_price = sum(int(item.product.unitPrice) * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price,})


#Sepete Ekle
@user_passes_test(lambda u: not u.is_superuser)
def addtocart(request, product_id):
    if request.method == 'POST':
        
        product = Product.objects.get(id=product_id)
        
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
           

    return redirect('order:view_cart')
    

#Sipariş Adetini arttır
@user_passes_test(lambda u: not u.is_superuser)
def addStock(request, id):
   
    cart_items = CartItem.objects.filter(id=id)

    cart_item = cart_items.first()
    

    cart_item.quantity+=1
    cart_item.save()

    
 
    return redirect('order:view_cart')

#Sipariş adetini azalt
@user_passes_test(lambda u: not u.is_superuser)
def lessStock(request,id):
    
    cart_items = CartItem.objects.filter(id=id)
    cart_item = cart_items.first()

    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        messages.info(request,"Ürün adeti en az 1 olabilir. Ürünü kaldırmak için lütfen sil'e tıklayınız..")
    
 
    return redirect('order:view_cart')


#Sepetten çıkar
@user_passes_test(lambda u: not u.is_superuser)
def remove(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()
    messages.success(request, "Ürün başarıyla silindi")
    return redirect('order:view_cart')







#Ödeme sayfası
@user_passes_test(lambda u: not u.is_superuser)
def payment(request):

    adres= Adres.objects.filter(user=request.user)

    context = {
        "adres":adres
    }


    return render(request,'payment.html',context=context)








#Kullanıcının Siparişleri
def orders(request):

    user = request.user
    order = Order.objects.filter(user=user)
    

    context = {
        "order": order

    }

    return render(request, 'orders.html', context=context)


#Tüm siparişler
@user_passes_test(lambda u:  u.is_superuser)
def order(request): 

    order = Order.objects.all()
    context={
        "order":order
    }
    return render(request,'order.html',context=context)



#Siparişi tamamla gibi bişey
@user_passes_test(lambda u: not u.is_superuser)
@login_required
def complete_order(request,id):
    user = request.user

   
    

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        messages.error(request, "Sepetiniz bulunamadı.")
        return redirect("order:view_cart")
    
    try:
        adres = Adres.objects.get(user=user,id=id)
    except Adres.DoesNotExist:
        messages.error(request,"Lütfen teslimat adresi ekleyiniz.")
        return redirect("order:view_address")
    
    
    title=str(adres.title)
    name_lastname=str(adres.name_lastname)
    adres=str(adres.adres)

    order = Order.objects.create(user=user, status='Bekliyor',title=title,adres=adres,name_lastname=name_lastname)

   


    for cart_item in CartItem.objects.filter(cart=cart):

        price = Decimal(cart_item.product.unitPrice) * cart_item.quantity

        if cart_item.product.unitsInStock < cart_item.quantity:
            messages.error(request, f"{cart_item.product.productName} için yeterli stok bulunmamaktadır. Mevcut stok: {cart_item.product.unitsInStock}")
            raise ValueError("Yetersiz stok")

        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=price,
        )
        cart_item.product.unitsInStock -= cart_item.quantity
        cart_item.product.save()

    cart.cartitem_set.all().delete()

    messages.success(request,"Sipariş başarıyla oluşturuldu")
    return redirect("order:view_cart")




#Sipariş Detayı
def order_detail(request, id):
    user = request.user
    order = Order.objects.get(id=id)
    item = OrderItem.objects.filter(order=order)
    
    
    

    return render(request, 'order_detail.html', {'order': order, 'item': item})









#Adresler Sayfası
@user_passes_test(lambda u: not u.is_superuser)
def view_address(request):
    user = request.user
    adres =Adres.objects.filter(user=user)

    context = {

        "adres" : adres
    }

    return render(request,"view_address.html",context=context)


#Adres Ekle
@user_passes_test(lambda u: not u.is_superuser)
def add_address(request):
    if request.method == 'POST':
        form = AdresForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request,"Adres başarıyla kaydedildi")
            return render(request, 'view_address.html')
    else:
        form = AdresForm()
    
    return render(request, 'add_address.html', {'form': form})


#Adres Güncelle
@user_passes_test(lambda u: not u.is_superuser)
def update_address(request, id):
    
    address = get_object_or_404(Adres, id=id, user=request.user)

    if request.method == 'POST':
        
        form = AdresForm(request.POST, instance=address)
        if form.is_valid():
            
            form.save()
            messages.success(request,"Adres başarıyla güncellendi")
            return redirect('order:view_address')
    else:
        form = AdresForm(instance=address)
    
    return render(request, 'update_address.html', {'form': form})




#Adres Sil
@user_passes_test(lambda u: not u.is_superuser)
def delete_address(request,id):

    address = get_object_or_404(Adres, id=id, user=request.user)
    address.delete()

    messages.success(request,"Adres başarıyla silindi")
    return redirect("order:view_address")





@user_passes_test(lambda u: u.is_superuser)
#Kargoları görüntüle (bekliyor olanları)
def create_cargos(request):

    pending_order = Order.objects.filter(status="Bekliyor")
    context = {
        "order": pending_order

    }

    return render(request, 'create_cargos.html', context=context)


#Tüm Kargolar
@user_passes_test(lambda u: u.is_superuser)
def cargos(request):

    cargos = Shipment.objects.all()
    context = {
        "cargos": cargos

    }

    return render(request, 'cargos.html', context=context)



@user_passes_test(lambda u: u.is_superuser)
#Kargoyu oluştur
def create_cargo(request,id):

    order = get_object_or_404(Order, id=id)

    
    new_shipment = Shipment.objects.create(
        user=request.user,
        order=order,
        status='Kargoya verildi'
    )

    order.status="Kargoya Verildi"
    order.save()

    messages.success(request,"Kargo oluşturuldu")

    return redirect('order:cargos')




#Kullanıcılar
@user_passes_test(lambda u: u.is_superuser)
def users(request):

    user = User.objects.all()
    context = {
        "user":user
    }
    return render(request,'user.html',context=context)
    
#Kullanıcının siparişleri
def users_orders(request, id):
    user = get_object_or_404(User, id=id)
  
    order = Order.objects.filter(user=user)
    
    context = {
        "order": order
    }


    return render(request, 'users_orders.html', context)