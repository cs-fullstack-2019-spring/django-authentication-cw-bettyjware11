from django import forms
from .models import FoodFitnessModel

class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model = FoodFitnessModel
        fields = ["userName", "calories", "date"]