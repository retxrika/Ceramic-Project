from django import forms

class CartForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class' : 'input-info', 'type' : 'email', 'autocomplete' : 'off'}))
    number = forms.CharField(label='Номер', widget=forms.TextInput(attrs={'class' : 'input-info', 'type' : 'tel'}))
    gift_sertificate = forms.CharField(label='Есть подарочный сертификат?', widget=forms.TextInput(attrs={'class' : 'input-info'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class' : 'input-info'}))
    type_dost = forms.NullBooleanField(label='Доставка', widget=forms.CheckboxInput(attrs={'class' : 'xz'}))
    name_of_user = forms.CharField(label='Получатель (ФИО полностью)', widget=forms.TextInput(attrs={'class' : 'input-info'}))
    street = forms.CharField(label='Улица', widget=forms.TextInput(attrs={'class' : 'input-info'}))
    house = forms.CharField(label='Дом', widget=forms.TextInput(attrs={'class' : 'input-home-room'}))
    room = forms.CharField(label='Квартира/офис', widget=forms.TextInput(attrs={'class' : 'input-home-room'}))
    commit = forms.CharField(required=False ,label='Комментарий к заказу', widget=forms.Textarea(attrs={'class' : 'input-commit'}))

