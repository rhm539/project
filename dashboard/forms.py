
from django import forms
from .models import Product, Order, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'AGroupName']
        labels = {
            'category': 'Accessories Name',
            'AGroupName': 'Accessories Group Name',
        }
        

class CategoryFormEdit(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'AGroupName', 'Status', 'use_quantity',
                  'stock_quantity', 'damage_quantity', 'total_quantity']
        labels = {
            'category': 'Accessories Name',
            'AGroupName': 'Accessories Group Name',
        }




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','quantity','category']

class ProductFormEdit(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','quantity','category','Status']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['AccessoriesName', 'product', 'order_quantity']
        labels = {
            'product': 'Product Detail',
            'AccessoriesName': 'Product Name',
        }


class OrderITForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['AccessoriesName','product', 'order_quantity', 'staff']
        labels = {
            'product': 'Product Detail',
            'AccessoriesName': 'Product Name',
        }


class OrderFormEdit(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity', 'OrStatus']
