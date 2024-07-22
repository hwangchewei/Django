from typing import Any
from django import forms
from .models import Userdata,Captcha,Blog

class RegisterForm(forms.ModelForm):
   
    password = forms.CharField(max_length=100,min_length=5,error_messages={'min_length':'password'})
    valid_p = forms.CharField(max_length=100,min_length=5)
    captcha = forms.CharField(max_length=4)
    
    class Meta:
        model = Userdata
        fields = ["email",'name']
        
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('valid_p')
        try:
            captche_valid = Captcha.objects.get(email=cleaned_data.get('email')).captcha
        except:
            captche_valid = 'false'
        captche = cleaned_data.get('captcha')
        if p1 != p2:
            raise forms.ValidationError('valid password error')
        elif captche_valid != captche:
            raise forms.ValidationError('captcha error')
        else:
            return cleaned_data
        
        
class LoginForm(forms.Form):
    
    password = forms.CharField(max_length=100,min_length=5)
    email = forms.EmailField()

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        exclude = ['name']