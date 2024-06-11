from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"   

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('update_account/',views.update_account,name="update_account"),
    path('account/',views.account,name="account"),
    

    

]