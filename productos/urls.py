from django.urls import path
from . import views

urlpatterns = [
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('vender_producto/<int:producto_id>/', views.vender_producto, name='vender_producto'),
    path('mostrar_boleta/<int:venta_id>/', views.mostrar_boleta, name='mostrar_boleta'),
    #path('generar_boleta_pdf/<int:venta_id>/', views.generar_boleta_pdf, name='generar_boleta_pdf'),
]
