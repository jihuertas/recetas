from django import forms
from .models import *

class FiltroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'refrigerado']

class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'refrigerado']

class IngredienteRecetaForm(forms.ModelForm):
    class Meta:
        model = IngredienteReceta
        fields = ['ingrediente', 'cantidad', 'unidad_medida']
