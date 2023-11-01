from django.shortcuts import render
from .models import Producto, Venta


def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/ver_productos.html', {'productos': productos})


def vender_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
        if cantidad > producto.stock:
            return render(request, 'producto/error.html', {'mensaje': 'No hay suficiente stock'})
        else:
            producto.stock -= cantidad
            producto.save()
            Venta.objects.create(producto=producto, cantidad=cantidad)
            return render(request, 'productos/venta_exitosa.html', {'producto': producto, 'cantidad': cantidad})

    return render(request, 'productos/vender_producto.html', {'producto': producto})


def mostrar_boleta(request, venta_id):
    venta = Venta.objects.get(pk=venta_id)
    return render(request, 'productos/mostrar_boleta.html', {'venta': venta})