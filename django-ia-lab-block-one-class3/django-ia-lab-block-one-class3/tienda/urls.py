from django.urls import path
from . import views

app_name="tienda"

urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.lista_productos, name="lista_productos"),
    path("pedidos/", views.lista_pedidos, name="lista_pedidos"),
    path("productos/<int:pk>/", views.detalle_producto, name="detalle_producto"),
    path("pedidos/<int:pk>/", views.detalle_pedido, name="detalle_pedido"),
    path("clientes/<int:pk>/", views.detalle_cliente, name="detalle_cliente"),

    path("productos/nuevo/", views.crear_producto, name="crear_producto"),
    path("productos/<int:pk>/editar/", views.editar_producto, name="editar_producto"),
    path("productos/<int:pk>/eliminar/", views.eliminar_producto, name="eliminar_producto"),
]