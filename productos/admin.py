from django.contrib import admin

from .models import Producto, Venta, Categoria


class Producto_Admin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'precio', 'stock')
    search_fields = ('codigo','nombre', 'precio')


class Categoria_Admin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'descripcion')
    search_fields = ['codigo','nombre']


class Venta_Admin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha')
    search_fields = ['fecha']


admin.site.register(Producto, Producto_Admin)
admin.site.register(Venta, Venta_Admin)
admin.site.register(Categoria, Categoria_Admin)
