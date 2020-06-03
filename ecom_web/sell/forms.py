from django import forms
from sell.models import Furniture

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture 
        fields = "__all__"