from django.db import models


# Definir clase Categoria con sus atributos
class Categoria(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Definir clase Producto con sus atributos
class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre


# Definir clase Venta con sus atributos
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} unidades"
