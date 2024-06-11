from django import forms
from .models import Cart,CartItem,Adres
from django.core.exceptions import ValidationError



class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity',] 


class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        
        fields= ['title','name_lastname','phoneNumber','eposta','adres']

        labels = {
            'title': 'Adres Başlığı',
            'name_lastname': 'İsim ve Soyisim',
            'phoneNumber': 'Telefon Numarası',
            'eposta': 'E-Posta',
            'adres': 'Adres Bilgileri',
        }


        def clean(self):
            cleaned_data = super().clean()

            phoneNumber = cleaned_data.get('phoneNumber')
            title = cleaned_data.get('title')
            adres= cleaned_data.get('adres')
            name_lastname = cleaned_data.get('name_lastname')
            eposta = cleaned_data.get('eposta')

            if phoneNumber and len(phoneNumber) != 10:
                raise ValidationError("Telefon numarası 10 haneli olmalıdır.")
            
            if title and len(title) < 3:
                raise ValidationError("Lütfen 3 veya daha fazla karakter giriniz.")
            
            if adres and len(adres) <1 :
                raise ValidationError("Lütfen bir adres giriniz.")
            
            if name_lastname and len(name_lastname) < 5:
                raise ValidationError("Lütfen 5 veya daha fazla karakter giriniz.")
            
            
            return cleaned_data

