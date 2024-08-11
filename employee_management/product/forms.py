# forms.py
from django import forms
from .models import Category,Jacket, Shirt, Pant, Shorts, T_shirt, Trouser

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        fields = '__all__'

class ShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        fields = '__all__'

class PantForm(forms.ModelForm):
    class Meta:
        model = Pant
        fields = '__all__'

class ShortsForm(forms.ModelForm):
    class Meta:
        model = Shorts
        fields = '__all__'

class TShirtForm(forms.ModelForm):
    class Meta:
        model = T_shirt
        fields = '__all__'

class TrouserForm(forms.ModelForm):
    class Meta:
        model = Trouser
        fields = '__all__'
