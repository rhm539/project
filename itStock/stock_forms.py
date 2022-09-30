from django import forms
from dashboard.models import AccessoriesGroup, Category
from itStock.models import InvoiceDetail, StockIssue
from django.contrib.auth.models import User

class InvoiceItemAddStockForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        labels = {
            'addstock': 'Add Stock',
        }
        fields = ['invoiceNumber', 'fundSerial',
                  'quantity', 'productName', 'addstock', 'category']
        widgets = {
            'invoiceNumber': forms.TextInput({'readonly': 'readonly'}),
            'fundSerial': forms.TextInput({'readonly': 'readonly'}),
            'quantity': forms.TextInput({'readonly': 'readonly'}),
            'addstock': forms.CheckboxInput(attrs={'required': 'True'}),
        }


class StockIssueForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=User.objects.order_by('username'))
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category'))
    class Meta:
        model = StockIssue
        fields = ['issueName', 'staff', 'category', 'quantity']


class AccessoriesGroupForm(forms.ModelForm):
    class Meta:
        model = AccessoriesGroup
        fields = ['AccessoriesName']
        labels = {
            'AccessoriesName': 'Accessories Group Name',
        }
