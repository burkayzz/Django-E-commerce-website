from typing import Any
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)




class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["first_name","last_name","email"]
    
        labels = {

            'first_name' : 'İsim',
            'last_name' : 'Soyisim',
            'email': 'E-Mail',


        }

        def clean(self) :
            cleaned_data = super().clean()

            first_name = self.cleaned_data("first_name")
            last_name = self.cleaned_data("last_name")
            email = self.changed_data("email")

            if first_name and len(first_name)<2:
                raise ValueError("En az 2 karakterli bir isim girmelisiniz.")
            if last_name and len(last_name)<2:
                raise ValueError("En az 2 karakterli bir soyisim girmelisiniz.")



            return cleaned_data

    
class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length=50,label = "Kullanıcı Adı")
    password = forms.CharField(max_length=25,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=25,label="Parolayı Doğrula",widget=forms.PasswordInput)

    def clean(self):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm  and password!=confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor..")
        
        values = {

            "username":username,
            "password":password,

        }

        return values 

