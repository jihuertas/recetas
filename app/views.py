from django.shortcuts import redirect, render
from .models import Ingrediente, CategoriaIngrediente
from .forms import *
from django.forms import formset_factory, modelformset_factory

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def ingredientes_lista(request):
    ingredientes = Ingrediente.objects.all()
    categorias = CategoriaIngrediente.objects.all()

    categoria_filtro = request.GET.get('categoria')
    refrigerado_filtro = request.GET.get('refrigerado')
    nombre_filtro = request.GET.get('nombre')

    if categoria_filtro:
        ingredientes = ingredientes.filter(categoria=categoria_filtro)
    if refrigerado_filtro:
        ingredientes = ingredientes.filter(refrigerado=True)
    if nombre_filtro:
        ingredientes = ingredientes.filter(nombre__icontains=nombre_filtro)

    formulario_filtro = FiltroIngredientesForm()

    return render(request, 'app/ingredientes_lista.html', {'categorias':categorias, 'ingredientes':ingredientes, 'formulario_filtro':formulario_filtro})

def ingredientes_nuevo(request):
    
    IngredienteFormSet = formset_factory(IngredientesForm, extra=3)

    if request.method == 'POST':
        formset = IngredienteFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)  # Aquí se tendría que guardar en la base de datos
            return redirect('inicio')
        else:
            print(formset.errors)
    else:
        formset = IngredienteFormSet()
    
    return render(request, 'app/ingredientes_nuevo.html', {'formularios':formset})


def ingredientes_nuevo_model(request):
        
    IngredienteFormSet = modelformset_factory(Ingrediente, form=IngredientesForm, extra=3)

    if request.method == 'POST':
        formset = IngredienteFormSet(request.POST,queryset=Ingrediente.objects.none())

        if formset.is_valid():
            formset.save()
            return redirect('ingredientes_lista')
        else:
            print(formset.errors)
    else:
        formset = IngredienteFormSet(queryset=Ingrediente.objects.none())
    
    return render(request, 'app/ingredientes_nuevo.html', {'formularios':formset})


def relaciones(request):
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'app/relaciones.html', {'recetas':recetas, 'ingredientes':ingredientes})