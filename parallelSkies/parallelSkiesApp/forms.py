from django import forms

class CityForm(forms.Form):
    city1 = forms.CharField(label='City 1', max_length=100)
    city2 = forms.CharField(label='City 2', max_length=100)
