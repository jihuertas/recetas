from django.shortcuts import redirect, render, get_object_or_404
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

def recetas_lista(request):
    recetas = Receta.objects.all()
    return render(request, 'app/recetas_lista.html', {'recetas':recetas})

def receta_detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    form = IngredienteRecetaForm()

    if request.method == 'POST':
        form = IngredienteRecetaForm(request.POST)
        if form.is_valid():
            form.instance.receta = receta
            form.save()
            return redirect('receta_detalle', pk=pk)
        else:
            print(form.errors)
    return render(request, 'app/receta_detalle.html', {'receta':receta, 'form':form})
    

def receta_detalle2(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    IngredienteRecetaFormSet = modelformset_factory(IngredienteReceta, form=IngredienteRecetaForm, extra=3)

    if request.method == 'POST':
        formset = IngredienteRecetaFormSet(request.POST,queryset=IngredienteReceta.objects.none())
        if formset.is_valid():
            for form in formset:
                form.instance.receta = receta
            formset.save()
            return redirect('receta_detalle', pk=pk)
        else:
            print(formset.errors)
    else:
        formset = IngredienteRecetaFormSet(queryset=IngredienteReceta.objects.none())
    return render(request, 'app/receta_detalle.html', {'receta':receta, 'formset':formset})
    

def receta_agregar_ingrediente(request, receta_pk, ingrediente_pk):
    receta = get_object_or_404(Receta, pk=receta_pk)
    ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_pk)

    receta.ingredientes.add(ingrediente)

    return redirect('receta_detalle', pk=receta_pk)