from django import forms
from Items.models import Items

class SellItemForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    image = forms.ImageField()
    description = forms.TextInput()
    price = forms.DecimalField(min_value=0.01, max_value=5000, max_digits=6, decimal_places=2)

    class Meta:
        model = Items
        fields = ['title', 'image', 'description', 'price']