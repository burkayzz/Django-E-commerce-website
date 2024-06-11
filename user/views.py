from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm,UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():

        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla Kayıt Oldunuz.")

        return redirect("index")
    context = {
        "form":form
        }
    return render(request,"register.html",context)

        

def account(request):

    return render(request,"account.html")


def update_account(request):

    user = request.user
    
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            
            messages.success(request,"Hesap bilgileri başarıyla güncellendi..")
            return redirect('user:account')
        
    else:
        form = UserForm(instance=user)

    return render(request,"update_account.html",{"form":form})





def loginUser(request):
    
    form = LoginForm(request.POST or None)

    context = {

        "form" : form
    }

    if form.is_valid():



        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password=password)
        
        if user is None:

            messages.info(request,"Kullanıcı adı veya şifre yanlış")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla giriş yapıldı")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)




def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
