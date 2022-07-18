from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import PartnersCategory, PartnersProduct

def partners(request):
    partners_categorys = PartnersCategory.objects.order_by()
    return render(request, 'partners/partners.html', {'partners_categorys' : partners_categorys})

def partners_detail(requset, slug):
    category = get_object_or_404(PartnersCategory, slug=slug)
    products = PartnersProduct.objects.order_by()
    context = {'products' : products, 'category' : category}
    return render(requset, 'partners/partners_detail.html', context)
