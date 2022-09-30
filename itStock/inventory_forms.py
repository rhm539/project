from django import forms
from dashboard.models import AccessoriesGroup, Category
from django.contrib.auth.models import User
from itStock.models import Inventory, InventoryAll, InventoryDetail
from user.models import Department




class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['productname']
        labels = {'productname': 'Inventory Name'}


class InventoryDetailForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=User.objects.order_by('username'))
    Processor = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='PROCESSOR'))))
    Motherboard = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='Motherboard'))))
    RAM1 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='RAM'))))
    RAM2 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='RAM'))))
    GraphicsCard = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='GraphicsCard'))))
    STORAGE1 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='STORAGE'))))
    STORAGE2 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='STORAGE'))))
    Monitor = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='MONITOR'))))
    Mouse = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='MOUSE'))))
    Keyboard = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='KEY BOARD'))))
    UPS = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='UPS'))))
    class Meta:
        model = InventoryDetail
        fields = ['staff', 'productname', 'Processor', 'Motherboard', 'RAM1', 'RAM2',
                  'GraphicsCard', 'STORAGE1', 'STORAGE2', 'Monitor', 'Mouse', 'Keyboard', 'UPS', 'remarks', 'status']
        widgets = {
            'productname': forms.HiddenInput(),
        }


class InventoryLaptopForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=User.objects.order_by('username'))
    Processor = forms.ModelChoiceField(queryset=Category.objects.filter( AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='PROCESSOR'))))
    RAM1 = forms.ModelChoiceField(queryset=Category.objects.filter(AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='RAM'))))
    RAM2 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='RAM'))))
    GraphicsCard = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='GraphicsCard'))))
    STORAGE1 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='STORAGE'))))
    STORAGE2 = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='STORAGE'))))
    Mouse = forms.ModelChoiceField(queryset=Category.objects.filter(
        AGroupName=(AccessoriesGroup.objects.get(AccessoriesName='MOUSE'))))


    class Meta:
        model = InventoryDetail
        fields = ['staff', 'LaptopBrand', 'productname', 'Processor', 'RAM1', 'RAM2',
                  'GraphicsCard', 'STORAGE1', 'STORAGE2', 'Mouse', 'Laptopbag', 'remarks', 'status']
        widgets = {
            'productname': forms.HiddenInput(),
        }


class InventoryMobileForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=User.objects.order_by('username'))
    class Meta:
        model = InventoryDetail
        fields = ['staff', 'MobileBrand', 'MobileMacc', 'Knox',
                  'productname', 'remarks', 'status']
        widgets = {
            'productname': forms.HiddenInput(),
        }


class InventoryIPphoneForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.order_by('dptName'))

    class Meta:
        model = InventoryAll
        fields = ['department', 'unit', 'Brand', 'ExtensionNumber', 'macaddress',
                  'productname', 'remarks', 'status']
        widgets = {
            'productname': forms.HiddenInput(),
        }


class InventoryALLphoneForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.order_by('dptName'))

    class Meta:
        model = InventoryAll
        fields = ['department', 'unit', 'Brand', 'model', 'macaddress',
                  'productname', 'remarks', 'status']
        widgets = {
            'productname': forms.HiddenInput(),
        }
