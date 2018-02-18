from django import forms
from .models import Spend

class SpendForm(forms.ModelForm):

    class Meta:
        model = Spend
        fields = ('created_data', 'customer', 'millage', 'cost')