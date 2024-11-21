from django import forms
from . models import contact
from django.forms import widgets
 
class ContactForm(forms.ModelForm):
    class Meta:
       model = contact
       exclude=()
       
       widgets={ 
           'name':widgets.TextInput(attrs={'class':'form-control','placeholder':"Your Name"}),
           'email':widgets.EmailInput(attrs={'class':'form-control','placeholder':"Email"}),
           'subject':widgets.NumberInput(attrs={'class':'form-control','placeholder':"Number"}),
           'message':widgets.Textarea(attrs={'class':'form-control','placeholder':"Message"})
       }