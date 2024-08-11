from django import forms
from .models import Client, StockSale
from product.models import Category

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'picture', 'email', 'whatsapp', 'gender', 'phone_number', 'remaining_balance']

class StockSaleForm(forms.ModelForm):
    product_name = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")
    class Meta:
        model = StockSale
        fields = ['client', 'product_name', 'product_price', 'product_quantity', 'payment_method', 'client_payed', 'discount_percentage']

class IDInputFormforbill(forms.Form):
    ids = forms.CharField(label='Enter IDs', help_text='Enter IDs separated by commas')
