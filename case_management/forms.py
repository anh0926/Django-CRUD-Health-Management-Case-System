from django import forms
from django.db.models import fields
from .models import Person, Referral 


class PersonForm(forms.ModelForm):  
    class Meta:  
        model = Person  
        fields = "__all__"  


class ReferralForm(forms.ModelForm):  
    class Meta:  
        model = Referral  
        fields = "__all__"  


      