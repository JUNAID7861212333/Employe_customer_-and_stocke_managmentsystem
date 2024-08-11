from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Jacket, Shirt, Pant, Shorts, T_shirt, Trouser
from .forms import CategoryForm, JacketForm, ShirtForm, PantForm, ShortsForm, TShirtForm, TrouserForm

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'  # Use this to refer to the data in the template



class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')



class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


# Jacket Views
class JacketListView(ListView):
    model = Jacket
    template_name = 'jacket/jacket_list.html'
    context_object_name = 'jackets'


class JacketDetailView(DetailView):
    model = Jacket
    template_name = 'jacket/jacket_detail.html'


class JacketCreateView(CreateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'jacket/jacket_form.html'
    success_url = reverse_lazy('jacket_list')


class JacketUpdateView(UpdateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'jacket/jacket_form.html'
    success_url = reverse_lazy('jacket_list')


class JacketDeleteView(DeleteView):
    model = Jacket
    template_name = 'jacket/jacket_confirm_delete.html'
    success_url = reverse_lazy('jacket_list')


# Shirt Views
class ShirtListView(ListView):
    model = Shirt
    template_name = 'shirts/shirt_list.html'
    context_object_name = 'shirts'


class ShirtDetailView(DetailView):
    model = Shirt
    template_name = 'shirts/shirt_detail.html'


class ShirtCreateView(CreateView):
    model = Shirt
    form_class = ShirtForm
    template_name = 'shirts/shirt_form.html'
    success_url = reverse_lazy('shirt_list')


class ShirtUpdateView(UpdateView):
    model = Shirt
    form_class = ShirtForm
    template_name = 'shirts/shirt_form.html'
    success_url = reverse_lazy('shirt_list')


class ShirtDeleteView(DeleteView):
    model = Shirt
    template_name = 'shirts/shirt_confirm_delete.html'
    success_url = reverse_lazy('shirt_list')


# Pant Views
class PantListView(ListView):
    model = Pant
    template_name = 'pent/pent_list.html'
    context_object_name = 'pants'

class PantDetailView(DetailView):
    model = Pant
    template_name = 'pent/pent_detail.html'
    context_object_name = 'pant'


class PantCreateView(CreateView):
    model = Pant
    form_class = PantForm
    template_name = 'pent/pent_form.html'
    success_url = reverse_lazy('pant_list')

class PantUpdateView(UpdateView):
    model = Pant
    form_class = PantForm
    template_name = 'pent/pent_form.html'
    success_url = reverse_lazy('pant_list')

class PantDeleteView(DeleteView):
    model = Pant
    template_name = 'pent/pent_confirm_delete.html'
    success_url = reverse_lazy('pant_list')


# Shorts Views
class ShortsListView(ListView):
    model = Shorts
    template_name = 'shorts/shorts_list.html'
    context_object_name = 'shortss'


class ShortsDetailView(DetailView):
    model = Shorts
    template_name = 'shorts/shorts_detail.html'


class ShortsCreateView(CreateView):
    model = Shorts
    form_class = ShortsForm
    template_name = 'shorts/shorts_form.html'
    success_url = reverse_lazy('shorts_list')


class ShortsUpdateView(UpdateView):
    model = Shorts
    form_class = ShortsForm
    template_name = 'shorts/shorts_form.html'
    success_url = reverse_lazy('shorts_list')


class ShortsDeleteView(DeleteView):
    model = Shorts
    template_name = 'shorts/shorts_confirm_delete.html'
    success_url = reverse_lazy('shorts_list')


# T-shirt Views
class TShirtListView(ListView):
    model = T_shirt
    template_name = 't_shirt/t_shirt_list.html'
    context_object_name = 't_shirts'


class TShirtDetailView(DetailView):
    model = T_shirt
    template_name = 't_shirt/t_shirt_detail.html'


class TShirtCreateView(CreateView):
    model = T_shirt
    form_class = TShirtForm
    template_name = 't_shirt/t_shirt_form.html'
    success_url = reverse_lazy('tshirt_list')


class TShirtUpdateView(UpdateView):
    model = T_shirt
    form_class = TShirtForm
    template_name = 't_shirt/t_shirt_form.html'
    success_url = reverse_lazy('tshirt_list')


class TShirtDeleteView(DeleteView):
    model = T_shirt
    template_name = 't_shirt/t_shirt_confirm_delete.html'
    success_url = reverse_lazy('tshirt_list')


# Trouser Views
class TrouserListView(ListView):
    model = Trouser
    template_name = 'trouser/trouser_list.html'
    context_object_name = 'trousers'



class TrouserDetailView(DetailView):
    model = Trouser
    template_name = 'trouser/trouser_detail.html'


class TrouserCreateView(CreateView):
    model = Trouser
    form_class = TrouserForm
    template_name = 'trouser/trouser_form.html'
    success_url = reverse_lazy('trouser_list')


class TrouserUpdateView(UpdateView):
    model = Trouser
    form_class = TrouserForm
    template_name = 'trouser/trouser_form.html'
    success_url = reverse_lazy('trouser_list')


class TrouserDeleteView(DeleteView):
    model = Trouser
    template_name = 'trouser/trouser_confirm_delete.html'
    success_url = reverse_lazy('trouser_list')
