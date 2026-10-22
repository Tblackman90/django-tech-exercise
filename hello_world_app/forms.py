from django import forms
from .models import Maintenance

# form for adding maintenance records
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['service', 'date', 'mileage', 'notes']

