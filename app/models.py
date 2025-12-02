from django.db import models

# Create your models here.

# class CategoriaChoices(models.TextChoices):
#     LEGUMBRE = "LE", "Legumbres"

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField('Ingrediente', related_name='recetas')

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