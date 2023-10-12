from django import forms
from .models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields =['Firstname','Lastname','username','Email','Password','mobileno']
        widgets = {
            'Firstname':forms.TextInput(attrs={'class':'form-control'}),
        }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)