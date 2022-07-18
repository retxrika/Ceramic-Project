from logging import info
import re
from main.forms import CartForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from yookassa.domain import request
from catalog.models import Category, User
from cart.cart import Cart
from cart.forms import CartAddProductForm
import uuid
from yookassa import Configuration, Payment, payment
from django.core.mail import send_mail
from .payments import Pay, SaveForm, GetCart, GetOrder
from .models import About, Slider, NumberOrder

# 5555555555554444


def pay(request):
    pay = Pay()
    p = pay.create_pay(request)
    Pay.obj = p
    print(Pay.obj.status, '1')

    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            SaveForm.email = form.cleaned_data['email']
            SaveForm.number = form.cleaned_data['number']
            SaveForm.gift_sertificate = form.cleaned_data['gift_sertificate']
            SaveForm.city = form.cleaned_data['city']
            SaveForm.name_of_user = form.cleaned_data['name_of_user']
            SaveForm.street = form.cleaned_data['street']
            SaveForm.house = form.cleaned_data['house']
            SaveForm.room = form.cleaned_data['room']
            SaveForm.commit = form.cleaned_data['commit']

        all_cart = GetCart.get_cart(request)
        names_of_items = ''
        for item in all_cart:
            quantity = ''
            quantity = item['quantity']
            names_of_items +=  str(item['product']) + '({})'.format(str(quantity)) + ', '
        GetOrder.names = names_of_items[:-2]
        GetOrder.price = str(all_cart.get_total_price())
        Cart(request).clear()
    return HttpResponseRedirect(p.confirmation.confirmation_url)


def pay_redirect(request):
    pay = Pay()
    pay_id = pay.obj.id
    p = Payment.find_one(pay_id)
    if p.status == 'succeeded':
        num = NumberOrder.objects.create(name=SaveForm.name_of_user)
        num.save()
        all_cart = GetCart.get_cart(request)
        all_text_user = '''Здравствуйте, {3}!

Ваш заказ: {0}
Оплачено: {1}р
Номер заказа: {2}'''.format(GetOrder.names, GetOrder.price, num.id, SaveForm.name_of_user)

        all_text_admin = '''ФИО: {0}
Номер: {1}
Адрес: {2}, {3} {4}, кв {5} 
Товары: {6}
Оплачено на сумму: {7}
Номер заказа: {8}
Комментарий к заказу: {9}'''.format(SaveForm.name_of_user, SaveForm.number, SaveForm.city, SaveForm.street, SaveForm.house, SaveForm.room, GetOrder.names, GetOrder.price, num.id, SaveForm.commit)
        print(all_text_admin)
        print('')
        print(all_text_user)
        mail = send_mail('Информация о заказе', all_text_user, 'ceramic-tam-tam@mail.ru', [SaveForm.email], 
        fail_silently=False)
        send_mail('Новый заказ', all_text_admin, 'ceramic-tam-tam@mail.ru', ['books141@mail.ru'], 
        fail_silently=False)
        if mail:
            print('Письмо отправлено')
        else:
            print('НЕ ПРОШЕЛ')
        print(SaveForm.email)
    return HttpResponseRedirect('http://localhost:8000')

def home(request):
    categorys = Category.objects.order_by()
    slider = Slider.objects.order_by()
    context = {'categorys' : categorys, 'slider' : slider}
    return render(request, 'main/home.html', context)

# def partners(request):
#     partners = Partner.objects.order_by()
#     categorys = Category.objects.order_by()
#     context = {'categorys' : categorys, 'partners' : partners}
#     return render(request, 'main/partners.html', context)

def about(request):
    abouts = About.objects.order_by()
    context = {'abouts' : abouts}
    return render(request, 'main/about.html', context)

def contact(request):
    return render(request, 'main/contact.html')






