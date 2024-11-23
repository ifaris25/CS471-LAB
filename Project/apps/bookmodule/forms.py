from django import forms
from apps.bookmodule.models import Book,Student,Address

class BookForm(forms.ModelForm):
    class Meta:
        model= Book  
        fields='__all__'
        
    title= forms.CharField(max_length=100,required=True,label='Title',widget=forms.TextInput())
    author= forms.CharField(max_length=100,required=True,label='Author',widget=forms.TextInput())
    price = forms.DecimalField(required=True,label='Price',initial=0)
    edition = forms.IntegerField(required=True,label='Edition',initial=1,widget=forms.NumberInput())
    
    
    
    

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    adress=forms.ModelChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.Select())
        
        
        