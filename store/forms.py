from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-50 border-none rounded-2xl py-5 px-6 text-sm font-bold focus:ring-2 focus:ring-accent/20 outline-none transition-all placeholder:text-slate-200',
                'placeholder': 'Node Designation'
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-50 border-none rounded-2xl py-4 px-6 text-sm font-bold focus:ring-2 focus:ring-accent/20 outline-none transition-all placeholder:text-slate-200',
                'placeholder': 'Module Designation'
            }),
            'price': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border-none rounded-2xl py-4 px-6 text-sm font-bold focus:ring-2 focus:ring-accent/20 outline-none transition-all'}),
            'stock': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border-none rounded-2xl py-4 px-6 text-sm font-bold focus:ring-2 focus:ring-accent/20 outline-none transition-all'}),
            'category': forms.Select(attrs={'class': 'w-full bg-slate-50 border-none rounded-2xl py-4 px-6 text-sm font-bold focus:ring-2 focus:ring-accent/20 outline-none transition-all appearance-none'}),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-slate-50 border-none rounded-[2rem] py-5 px-6 text-sm font-medium focus:ring-2 focus:ring-accent/20 outline-none transition-all min-h-[120px]',
                'rows': 4
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'absolute inset-0 opacity-0 cursor-pointer'}),
        }