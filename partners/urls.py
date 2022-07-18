from django.urls import path
from . import views

app_name = 'partners'


urlpatterns = [
    path('', views.partners, name='partners'),
    path('category/<str:slug>/', views.partners_detail, name='partners_detail'),
    # path('category/<str:slug>/', views.category_detail, name='category_detail'),
    # path('product/<str:slug>', views.product_detail, name='product_detail'),
]