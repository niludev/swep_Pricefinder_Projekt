from django import forms

class CarDetailsForm(forms.Form):
    manufacturer = forms.CharField(max_length=100, required=True)
    model = forms.CharField(max_length=100, required=True)
    prod_year = forms.IntegerField(required=True)
    category = forms.CharField(max_length=100, required=False)
    leather_interior = forms.BooleanField(required=False)
    fuel_type = forms.CharField(max_length=50, required=True)
    engine_volume = forms.DecimalField(max_digits=5, decimal_places=2, required=True)
    mileage = forms.IntegerField(required=True)
    cylinders = forms.IntegerField(required=True)
    gear_box_type = forms.CharField(max_length=50, required=False)
    drive_wheels = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=50, required=True)
    airbags = forms.IntegerField(required=True)