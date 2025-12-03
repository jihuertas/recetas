from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(CategoriaIngrediente)
admin.site.register(Receta)
admin.site.register(IngredienteReceta)
