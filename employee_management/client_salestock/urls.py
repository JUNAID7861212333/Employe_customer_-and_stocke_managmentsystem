# urls.py in client_salestock app

from django.urls import path
from . import views
from .views import stocksale_create, get_products_by_category

urlpatterns = [
    # Client URLs
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/create/', views.client_create, name='client_create'),  # Ensure this path is correctly defined
    path('clients/<int:pk>/edit/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    # StockSale URLs
    path('stocksales/', views.stocksale_list, name='stocksale_list'),
    path('stocksales/<int:pk>/', views.stocksale_detail, name='stocksale_detail'),
    # path('bill/<int:pk>/', views.bill, name='bill'),
    path('stocksales/new/', views.stocksale_create, name='stocksale_create'),
    path('stocksales/<int:pk>/edit/', views.stocksale_update, name='stocksale_update'),
    path('stocksales/<int:pk>/delete/', views.stocksale_delete, name='stocksale_delete'),

    # Payment Processing URLs (assuming these are separate from client_salestock)
    path('process_payment/<int:client_id>/<str:product_name>/<str:product_price>/<str:payment_amount>/', views.process_payment, name='process_payment'),
    path('process_payment/<int:client_id>/<str:product_name>/<str:product_price>/<str:payment_amount>/<str:discount_amount>/', views.process_payment, name='process_payment_with_discount'),
    path('get_products_by_category/', get_products_by_category, name='get_products_by_category'),
    
    
    #bill
    # path('fetch_data_for_bill/', views.fetch_data_for_bill, name='fetch_data_for_bill'),
    path('form/', views.form_page, name='form_page'),
    path('fetch_data_for_bill/', views.fetch_data_for_bill, name='fetch_data_for_bill'),



]
