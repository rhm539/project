from django import forms
from .models import Invoice, Supplier, Fund, FundDetail, InvoiceDetail



class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ['fundName','unit']
        labels ={
            'fundName': 'Fund Name',
            'unit':'Unit Name',
        }
        widgets = {
            'fundName': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplierName','contactName','address','email','contactNumber','status']


class InvoiceFormPdf(forms.ModelForm):
     class Meta:
        model = Invoice
        fields=['invoiceNumber','unit','supplierName','status','date', 'pdf']   
        widgets = {
            'invoiceNumber': forms.TextInput({'readonly':'readonly'}),
        }     

########### forset
class InvoiceForm(forms.ModelForm):
     class Meta:
        model = Invoice
        fields = ['unit','invoiceNumber','supplierName','status','date']
        widgets = {
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'invoiceNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'supplierName': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }
   

####### forset
class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            'productName', 'quantity', 'unitprice', 'macaddress', 'warranty', 'category',
            ]
        widgets = {
            'productName': forms.Textarea(attrs={'class': 'formset-field form-control', 'rows': 3, 'cols': 30}),
            'quantity': forms.NumberInput(attrs={'class': 'formset-field form-control'}),
            'unitprice': forms.NumberInput(attrs={'class': 'formset-field form-control'}),
            'macaddress': forms.TextInput(attrs={'class': 'formset-field form-control'}),
            'warranty': forms.Select(attrs={'class': 'formset-field form-control'}),
            'category': forms.Select(attrs={'class': 'formset-field form-control'}),

            
            
  
		}

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            'productName','quantity','unitprice'
        ]


class InvoiceItemEditForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = ['invoiceNumber', 'productName', 'quantity',
                  'unitprice', 'warranty', 'macaddress', 'fundSerial', 'category']
        widgets = {
            'invoiceNumber': forms.TextInput({'readonly':'readonly'}),
    		}




class InvoiceItemAddForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = ['productName', 'quantity',
                  'unitprice', 'warranty', 'macaddress']













######
class FundDetailForm(forms.ModelForm):
    class Meta:
        model = FundDetail
        fields = [
            'particulars','buyer','style','quantity','rate','remarks',
            ]
        widgets = {
            'particulars': forms.Textarea(attrs={'class': 'form-control formset-field', 'rows': 3, 'cols': 22}),
           	'buyer': forms.TextInput(attrs={'class': 'form-control formset-field'}),
            'style': forms.TextInput(attrs={'class': 'form-control formset-field'}),
           	'quantity': forms.NumberInput(attrs={'class': 'form-control formset-field', 'maxlength': 4, 'size': 4}),
            'rate': forms.NumberInput(attrs={'class': 'form-control formset-field'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control formset-field', 'rows': 3, 'cols': 22}),
		}

class FundItemForm(forms.ModelForm):
    class Meta:
        model = FundDetail
        fields = [
            'particulars','buyer','style','quantity','rate','remarks',
            ]

class FundDetailInvForm(forms.ModelForm):
    class Meta:
        model = FundDetail
        fields = [
            'invoiceNumber','particulars','buyer','style','quantity','rate',
            ]
        widgets = {
            'particulars': forms.TextInput({'readonly':'readonly'}),
            'buyer': forms.TextInput({'readonly':'readonly'}),
            'style': forms.TextInput({'readonly':'readonly'}),
            'quantity': forms.TextInput({'readonly':'readonly'}),
            'rate': forms.TextInput({'readonly':'readonly'}),
		}

