from django import forms

# Форма заполнения заказа
class CartForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : ''}))
    surname = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : ''}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : '', 'type' : 'email', 'autocomplete' : 'off'}))
    number = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : '', 'type' : 'tel'}))
    
    commit = forms.CharField(required=False ,label='Комментарий к заказу', widget=forms.Textarea(attrs={'class' : ''}))

