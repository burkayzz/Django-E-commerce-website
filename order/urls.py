from django.contrib import admin
from django.urls import path
from . import views
app_name = "order"

urlpatterns = [

   path('cart/',views.view_cart,name="view_cart"),
   path('addtocart/<int:product_id>/',views.addtocart,name="addtocart"),
   path('lessstock/<int:id>/',views.lessStock,name="lessStock"),
   path('addstock/<int:id>',views.addStock,name="addStock"),
   path('remove/<int:id>/',views.remove,name="remove"),

   
   path('payment/',views.payment,name="payment"),
   path('complete_order/<int:id>',views.complete_order,name="complete_order"),
   path('orders/',views.orders,name="orders"),
   path('orders/<int:id>',views.order_detail,name="order_detail"),
   path('users_orders/<int:id>',views.users_orders,name="users_orders"),
   path('order/',views.order,name="order"),


   path('add_address/',views.add_address,name="add_address"),
   path('view_address/',views.view_address,name="view_address"),
   path('update_address/<int:id>/', views.update_address, name='update_address'),
   path('delete_address/<int:id>/',views.delete_address,name="delete_address"),


   path('users/',views.users,name="users"),




   path('cargos/',views.cargos,name="cargos"),
   path('create_cargos/',views.create_cargos,name="create_cargos"),
   path('create_cargo/<int:id>',views.create_cargo,name="create_cargo"),



   
    
]