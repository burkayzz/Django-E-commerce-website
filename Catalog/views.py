from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Product,Category,Brand
from .forms import ProductForm,CategoryForm,BrandForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

#Anasayfa
def index(request):

    category = Category.objects.all()

    context = {
        "category":category
    }

    return render(request,"index.html",context=context)



#Ürün ekle
@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request,"Ürün başarıyla kaydedildi")
            return redirect('Catalog:product')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})




#Ürün Güncelle
@user_passes_test(lambda u: u.is_superuser)
def update_product(request,id):
 
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        
        form = ProductForm(request.POST, request.FILES, instance=product )
        if form.is_valid():
            
            form.save()
            messages.success(request,"Ürün bilgileri başarıyla güncellendi")
            return redirect('Catalog:product')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'update_product.html', {'form': form})


#Ürün sil
@user_passes_test(lambda u: u.is_superuser)
def delete_product(request,id):

    product = get_object_or_404(Product, id=id)
    product.delete()

    messages.success(request,"Ürün başarıyla silindi")
    return redirect("Catalog:product")


#Ürünler 
def product(request):

    keyword = request.GET.get("keyword")

    if keyword:
       product = Product.objects.filter(productName__contains=keyword)
       return render(request,"product.html",{"product":product}) 


    product = Product.objects.filter(unitsInStock__gt=0)
    context = {
        "product":product
    }


    return render(request,"product.html",context)





#Ürün detay sayfası
def detail(request, id):

    product = Product.objects.filter(id = id).first
    return render(request,"detail.html",{"product":product})        





#Kategoriye ait ürünler
def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})


#Kategori ekle
@user_passes_test(lambda u: u.is_superuser)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request,"Kategori başarıyla oluşturuldu")
            return redirect('Catalog:categories')
    else:
        form = CategoryForm()
    
    return render(request, 'add_category.html', {'form': form})


#Kategoriler
@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    category = Category.objects.all()
    context = {
        "category":category
    }

    return render(request,'categories.html',context=context)


#Kategori sil
@user_passes_test(lambda u: u.is_superuser)
def delete_category(request,id):
    category = get_object_or_404(Category, id=id)
    category.delete()

    messages.success(request,"Kategori başarıyla silindi")
    return redirect("Catalog:categories")

#Kategori güncelle
@user_passes_test(lambda u: u.is_superuser)
def update_category(request,id):
 
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        
        form = CategoryForm(request.POST, instance=category )
        if form.is_valid():
            
            form.save()
            messages.success(request,"Kategori bilgileri başarıyla güncellendi")
            return redirect('Catalog:categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'update_category.html', {'form': form})




#Marka ekle
@user_passes_test(lambda u: u.is_superuser)
def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            messages.success(request,"Marka başarıyla oluşturuldu")
            return redirect('Catalog:brands')
    else:
        form = CategoryForm()
    
    return render(request, 'add_brand.html', {'form': form})

#Markalar
@user_passes_test(lambda u: u.is_superuser)
def brands(request):
    brand = Brand.objects.all()
    context = {
        "brand":brand
    }

    return render(request,'brands.html',context=context)


#Marka sil
@user_passes_test(lambda u: u.is_superuser)
def delete_brand(request,id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()

    messages.success(request,"Marka başarıyla silindi")
    return redirect("Catalog:brands")
    

    
@user_passes_test(lambda u: u.is_superuser)
def update_brand(request,id):
 
    brand = get_object_or_404(Brand, id=id)

    if request.method == 'POST':
        
        form = BrandForm(request.POST, instance=brand )
        if form.is_valid():
            
            form.save()
            messages.success(request,"Marka bilgileri başarıyla güncellendi")
            return redirect('Catalog:brands')
    else:
        form = BrandForm(instance=brand)
    
    return render(request, 'update_brand.html', {'form': form})