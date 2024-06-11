from django.contrib import admin
from django.urls import path
from . import views
app_name = "Catalog"

urlpatterns = [
    path('product/',views.product,name="product"),
    path('add_product/',views.add_product,name="add_product"),
    path('update_product/<int:id>/',views.update_product,name="update_product"),
    path('delete_product/<int:id>/',views.delete_product,name="delete_product"),
    path('product/<int:id>',views.detail,name="detail"),
    

    path('update_category/<int:id>/',views.update_brand,name="update_category"),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('categories/',views.categories,name="categories"),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),


    path('update_brand/<int:id>/',views.update_brand,name="update_brand"),
    path('brands/',views.brands,name="brands"),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('delete_brand/<int:id>/', views.delete_brand, name='delete_brand'),
]

    



