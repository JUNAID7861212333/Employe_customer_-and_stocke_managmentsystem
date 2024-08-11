# urls.py
from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    JacketListView, JacketDetailView, JacketCreateView, JacketUpdateView, JacketDeleteView,
    ShirtListView, ShirtDetailView, ShirtCreateView, ShirtUpdateView, ShirtDeleteView,
    PantListView, PantDetailView, PantCreateView, PantUpdateView, PantDeleteView,
    ShortsListView, ShortsDetailView, ShortsCreateView, ShortsUpdateView, ShortsDeleteView,
    TShirtListView, TShirtDetailView, TShirtCreateView, TShirtUpdateView, TShirtDeleteView,
    TrouserListView, TrouserDetailView, TrouserCreateView, TrouserUpdateView, TrouserDeleteView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/new/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Jacket URLs
    path('jackets/', JacketListView.as_view(), name='jacket_list'),
    path('jackets/<int:pk>/', JacketDetailView.as_view(), name='jacket_detail'),
    path('jackets/new/', JacketCreateView.as_view(), name='jacket_create'),
    path('jackets/<int:pk>/edit/', JacketUpdateView.as_view(), name='jacket_update'),
    path('jackets/<int:pk>/delete/', JacketDeleteView.as_view(), name='jacket_delete'),
    
    # Shirt URLs
    path('shirts/', ShirtListView.as_view(), name='shirt_list'),
    path('shirts/<int:pk>/', ShirtDetailView.as_view(), name='shirt_detail'),
    path('shirts/new/', ShirtCreateView.as_view(), name='shirt_create'),
    path('shirts/<int:pk>/edit/', ShirtUpdateView.as_view(), name='shirt_update'),
    path('shirts/<int:pk>/delete/', ShirtDeleteView.as_view(), name='shirt_delete'),

    # Pant URLs
    path('pants/', PantListView.as_view(), name='pant_list'),
    path('pants/<int:pk>/', PantDetailView.as_view(), name='pant_detail'),
    path('pants/new/', PantCreateView.as_view(), name='pant_create'),
    path('pants/<int:pk>/edit/', PantUpdateView.as_view(), name='pant_update'),
    path('pants/<int:pk>/delete/', PantDeleteView.as_view(), name='pant_delete'),

    # Shorts URLs
    path('shorts/', ShortsListView.as_view(), name='shorts_list'),
    path('shorts/<int:pk>/', ShortsDetailView.as_view(), name='shorts_detail'),
    path('shorts/new/', ShortsCreateView.as_view(), name='shorts_create'),
    path('shorts/<int:pk>/edit/', ShortsUpdateView.as_view(), name='shorts_update'),
    path('shorts/<int:pk>/delete/', ShortsDeleteView.as_view(), name='shorts_delete'),

    # T-shirt URLs
    path('tshirts/', TShirtListView.as_view(), name='tshirt_list'),
    path('tshirts/<int:pk>/', TShirtDetailView.as_view(), name='tshirt_detail'),
    path('tshirts/new/', TShirtCreateView.as_view(), name='tshirt_create'),
    path('tshirts/<int:pk>/edit/', TShirtUpdateView.as_view(), name='tshirt_update'),
    path('tshirts/<int:pk>/delete/', TShirtDeleteView.as_view(), name='tshirt_delete'),

    # Trouser URLs
    path('trousers/', TrouserListView.as_view(), name='trouser_list'),
    path('trousers/<int:pk>/', TrouserDetailView.as_view(), name='trouser_detail'),
    path('trousers/new/', TrouserCreateView.as_view(), name='trouser_create'),
    path('trousers/<int:pk>/edit/', TrouserUpdateView.as_view(), name='trouser_update'),
    path('trousers/<int:pk>/delete/', TrouserDeleteView.as_view(), name='trouser_delete'),
]
