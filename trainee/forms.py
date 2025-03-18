from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ["trainee"]  # Ensure this matches your model field name
