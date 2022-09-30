from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Department, Profile 


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','officeID','officeLocation','department','designation','phone', 'address', 'image','signature']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        labels = {'email': 'E-mail'}

class addUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'User Name',
            'email': 'E-mail'
            }


class addProfileForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.order_by('dptName'))
    class Meta:
        model = Profile
        fields = ['loginuser', 'name', 'officeID',
                  'officeLocation', 'department']
        labels = {
            'loginuser': 'Login Name',
            'name': 'Name',
            'officeID': 'Office ID',
            'officeLocation': 'Unit Name',
            'department': 'Department Name'
            }


class addDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dptName']
        labels = {'dptName': 'Department Name'}
