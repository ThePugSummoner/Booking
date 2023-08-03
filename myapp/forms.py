from django.forms import ModelForm
from .models import Booking
from django import forms

# ModelForm: MenuForm
class MenuForm(forms.Form):
    item_name = forms.CharField(max_length = 200)
    category = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000)

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

