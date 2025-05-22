from django import forms
from .models import Branch

class branchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'email', 'phone_number', 'address', 'gps_location', 'is_headbranch']