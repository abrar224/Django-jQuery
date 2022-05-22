from django import forms
from .models import User

class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','batch','dept']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'batch':forms.TextInput(attrs={'class':'form-control', 'id':'batchid'}),
            'dept':forms.TextInput(attrs={'class':'form-control', 'id':'deptid'})
            }

