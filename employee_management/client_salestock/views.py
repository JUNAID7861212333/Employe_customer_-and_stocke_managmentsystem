from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Client, StockSale
from .forms import ClientForm, StockSaleForm
from decimal import Decimal
from product.models import Category 

# Client Views

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_salestock/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_salestock/client_detail.html', {'client': client})

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)  # Redirect to client detail page after creation
    else:
        form = ClientForm()
    return render(request, 'client_salestock/client_form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_salestock/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'client_salestock/client_confirm_delete.html', {'client': client})

# StockSale Views

def stocksale_list(request):
    stocksales = StockSale.objects.select_related('client').all()
    for sale in stocksales:
        sale.total_order_price = sale.product_price * sale.product_quantity
    return render(request, 'client_salestock/stocksale_list.html', {'stocksales': stocksales})


def stocksale_detail(request, pk):
    stocksale = get_object_or_404(StockSale, pk=pk)
    return render(request, 'client_salestock/stocksale_detail.html', {'stocksale': stocksale})





# from django.shortcuts import render
# from datetime import datetime

# def invoice_view(request):
#     # Example context with current date and time
#     context = {
#         'bill': {
#             'client': {
#                 'id': '12345'  # Replace with actual client ID
#             }
#         },
#         'current_date': datetime.now().strftime("%d-%m-%Y"),
#         'current_time': datetime.now().strftime("%I:%M %p")
#     }
#     return render(request, 'client_salestock/bill.html', context)


# def bill(request, pk):
#     bill = get_object_or_404(StockSale, pk=pk)
#     return render(request, 'client_salestock/bill.html', {'bill': bill})
















# def stocksale_create(request):
#     if request.method == "POST":
#         form = StockSaleForm(request.POST)
#         if form.is_valid():
#             client = form.cleaned_data['client']
#             product_name = form.cleaned_data['product_name']
#             product_price = form.cleaned_data['product_price']
#             product_quantity = form.cleaned_data['product_quantity']
#             payment_method = form.cleaned_data['payment_method']
#             client_payed = form.cleaned_data['client_payed']
#             discount_percentage = form.cleaned_data['discount_percentage']

#             sales = form.save(commit=False)

#             total_order_count = product_price * product_quantity
#             after_discount = total_order_count * (1 - discount_percentage / 100)
#             remaining_payment = after_discount - client_payed

#             # Update the client's remaining balance
#             client.remaining_balance += remaining_payment
#             client.save()

#             sales.total_order_count = total_order_count
#             sales.after_discount = after_discount
#             sales.save()

#             return redirect('stocksale_detail', pk=sales.pk)
#     else:
#         form = StockSaleForm()

#     return render(request, 'client_salestock/stocksale_form.html', {'form': form})




from product.models import Jacket, Pant, Shirt, Shorts, T_shirt, Trouser

def stocksale_create(request):
    if request.method == "POST":
        form = StockSaleForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            product_name = form.cleaned_data['product_name']
            product_price = form.cleaned_data['product_price']
            product_quantity = form.cleaned_data['product_quantity']
            payment_method = form.cleaned_data['payment_method']
            client_payed = form.cleaned_data['client_payed']
            discount_percentage = form.cleaned_data['discount_percentage']

            # Determine the product model
            category = Category.objects.get(name=product_name)
            product = None
            if Jacket.objects.filter(fabric_type=category).exists():
                product = Jacket.objects.filter(fabric_type=category).first()
            elif Pant.objects.filter(fabric_type=category).exists():
                product = Pant.objects.filter(fabric_type=category).first()
            elif Shirt.objects.filter(fabric_type=category).exists():
                product = Shirt.objects.filter(fabric_type=category).first()
            elif Shorts.objects.filter(fabric_type=category).exists():
                product = Shorts.objects.filter(fabric_type=category).first()
            elif T_shirt.objects.filter(fabric_type=category).exists():
                product = T_shirt.objects.filter(fabric_type=category).first()
            elif Trouser.objects.filter(fabric_type=category).exists():
                product = Trouser.objects.filter(fabric_type=category).first()

            if product:
                product.quantity -= product_quantity
                product.save()

            sales = form.save(commit=False)
            total_order_count = product_price * product_quantity
            after_discount = total_order_count * (1 - discount_percentage / 100)
            remaining_payment = after_discount - client_payed

            # Update the client's remaining balance
            client.remaining_balance += remaining_payment
            client.save()

            sales.total_order_count = total_order_count
            sales.after_discount = after_discount
            sales.save()

            return redirect('stocksale_detail', pk=sales.pk)
    else:
        form = StockSaleForm()

    return render(request, 'client_salestock/stocksale_form.html', {'form': form})

from django.http import JsonResponse
from product.models import Jacket, Pant, Shirt, Shorts, T_shirt, Trouser

def get_products_by_category(request):
    category_id = request.GET.get('category_id')
    products = []

    jackets = Jacket.objects.filter(fabric_type_id=category_id)
    pants = Pant.objects.filter(fabric_type_id=category_id)
    shirts = Shirt.objects.filter(fabric_type_id=category_id)
    shorts = Shorts.objects.filter(fabric_type_id=category_id)
    tshirts = T_shirt.objects.filter(fabric_type_id=category_id)
    trousers = Trouser.objects.filter(fabric_type_id=category_id)

    for product in list(jackets) + list(pants) + list(shirts) + list(shorts) + list(tshirts) + list(trousers):
        products.append({'id': product.id, 'name': str(product)})

    return JsonResponse({'products': products})




def stocksale_update(request, pk):
    stocksale = get_object_or_404(StockSale, pk=pk)
    if request.method == "POST":
        form = StockSaleForm(request.POST, instance=stocksale)
        if form.is_valid():
            stocksale = form.save()
            return redirect('stocksale_detail', pk=stocksale.pk)
    else:
        form = StockSaleForm(instance=stocksale)
    return render(request, 'client_salestock/stocksale_form.html', {'form': form})

def stocksale_delete(request, pk):
    stocksale = get_object_or_404(StockSale, pk=pk)
    if request.method == "POST":
        stocksale.delete()
        return redirect('stocksale_list')
    return render(request, 'client_salestock/stocksale_confirm_delete.html', {'stocksale': stocksale})

# Payment Processing View

def process_payment(request, client_id):
    if request.method == "POST":
        form = StockSaleForm(request.POST)
        if form.is_valid():
            product_price = form.cleaned_data['product_price']
            product_quantity = form.cleaned_data['product_quantity']
            payment_amount = form.cleaned_data['payment_amount']
            discount_percentage = form.cleaned_data.get('discount_percentage', 0)
            
            client = get_object_or_404(Client, pk=client_id)
            
            product_price = Decimal(product_price)
            product_quantity = int(product_quantity)
            payment_amount = Decimal(payment_amount)
            discount_percentage = Decimal(discount_percentage)
            
            # Calculate total order count
            total_order_count = product_quantity  # Example calculation
            
            # Calculate total order price
            total_order_price = product_price * product_quantity
            
            # Apply discount
            discount_amount = (discount_percentage / 100) * total_order_price
            discounted_price = total_order_price - discount_amount
            
            remaining_balance = client.remaining_balance
            new_remaining_balance = remaining_balance + (discounted_price - payment_amount)
            
            # Update the client's remaining balance
            client.remaining_balance = new_remaining_balance if new_remaining_balance > 0 else 0
            client.save()
            
            # Create a new StockSale record
            stocksale = form.save(commit=False)
            stocksale.client = client
            stocksale.total_order_count = total_order_count
            stocksale.product_price = product_price
            stocksale.product_quantity = product_quantity
            stocksale.payment_amount = payment_amount
            stocksale.discounted = True if discount_percentage > 0 else False
            stocksale.save()
            
            return redirect('stocksale_detail', pk=stocksale.pk)
    else:
        form = StockSaleForm()
    
    return render(request, 'client_salestock/stocksale_form.html', {'form': form})





from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import StockSale, Client
from .forms import IDInputFormforbill
from datetime import datetime
import inflect

def form_page(request):
    form = IDInputFormforbill()
    return render(request, 'client_salestock/test_bill.html', {'form': form})

def bill_context():
    """Return the context for the bill view."""
    return {
        'current_date': datetime.now().strftime("%d-%m-%Y"),
        'current_time': datetime.now().strftime("%I:%M %p"),
    }

def fetch_data_for_bill(request):
    if request.method == 'POST':
        form = IDInputFormforbill(request.POST)
        if form.is_valid():
            ids = form.cleaned_data['ids']
            id_list = [int(id.strip()) for id in ids.split(',') if id.strip()]
            if id_list:
                employees = StockSale.objects.filter(id__in=id_list)
                
                # Calculate total after_discount
                total_after_discount = employees.aggregate(total_discount=Sum('after_discount'))['total_discount'] or 0
                total_after_discount_rounded = round(total_after_discount, 2)
                p = inflect.engine()
                total_after_discount_words = p.number_to_words(total_after_discount_rounded, andword=', and')

                # Get unique client IDs and their remaining balances
                client_ids = employees.values_list('client_id', flat=True).distinct()
                remaining_balances = []
                for client_id in client_ids:
                    client = Client.objects.get(id=client_id)
                    remaining_balances.append(client.remaining_balance)

            else:
                employees = []
                total_after_discount = 0
                total_after_discount_rounded = 0
                total_after_discount_words = 'zero'
                remaining_balances = []

            # Get context from the bill function
            bill_ctx = bill_context()

            # Get unique client IDs from the fetched records
            client_ids = employees.values_list('client_id', flat=True).distinct()
            client_ids = list(client_ids)  # Convert QuerySet to list


            # Combine form, bill context, total discount context, and remaining balances
            context = {
                'form': form,
                'employees': employees,
                'total_after_discount': total_after_discount_rounded,
                'total_after_discount_words': total_after_discount_words,
                'remaining_balances': remaining_balances,
                'client_ids': client_ids,
                **bill_ctx
            }

            return render(request, 'client_salestock/bill.html', context)
    else:
        return redirect('form_page')
