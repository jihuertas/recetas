from django.db import models

# Create your models here.

# class CategoriaChoices(models.TextChoices):
#     LEGUMBRE = "LE", "Legumbres"



class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField('Ingrediente', through='IngredienteReceta')

    def __str__(self) -> str:
        return f"{self.nombre}"

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)
    refrigerado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria})"
    
class IngredienteReceta(models.Model):
    class MedidaChoices(models.TextChoices):
        GRAMOS = "gr", "Gramos"
        KILOGRAMOS = "kg", "Kilogramos"
        LITROS = "l", "Litros"
        MILILITROS = "ml", "Mililitros"
        UNIDADES = "u", "Unidades"

    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    unidad_medida = models.CharField(max_length=2, choices=MedidaChoices.choices, default=MedidaChoices.UNIDADES)

    def __str__(self) -> str:
        return f"{self.cantidad} {self.unidad_medida} de {self.ingrediente.nombre} en {self.receta.nombre}"
    
    class Meta:
        unique_together = ('receta', 'ingrediente')