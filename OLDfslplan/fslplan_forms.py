from django import forms

from fslplan.fslplan_models import Buyer, SetupDay, SetupLine, Style, Unit


########### forset
class DaysetupForm(forms.ModelForm):
    unit = forms.ModelChoiceField(queryset=Unit.objects.order_by('name'))
    buyer = forms.ModelChoiceField(queryset=Buyer.objects.order_by('name'))
    style = forms.ModelChoiceField(queryset=Style.objects.order_by('name'))
    class Meta:
        model = SetupDay
        fields = ['unit', 'buyer', 'style', 'DayTerget',
                  'WorkHour', 'EstimateWorkDay', 'date']
        widgets = {
            'date': forms.DateInput({'type': 'date'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['style'].queryset = Style.objects.none()

            if 'buyer' in self.data:
                try:
                    buyer = int(self.data.get('buyer'))
                    self.fields['city'].queryset = Style.objects.filter(
                        buyer=buyer).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['style'].queryset = self.instance.buyer.style_set.order_by('name')




class SetupLineForm(forms.ModelForm):
    class Meta:
        model = SetupLine
        fields = [
            'H_8_9', 'H_9_10', 'H_10_11', 'H_11_12', 'H_12_13',
            'H_14_15', 'H_15_16', 'H_16_17', 'H_17_18', 'H_18_19',
            'H_19_20', 'H_20_21', 'H_21_22',
            'LineWIP', 'DataLock'
        ]


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name']


class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = ['name', 'StyleSMV', 'buyer']
