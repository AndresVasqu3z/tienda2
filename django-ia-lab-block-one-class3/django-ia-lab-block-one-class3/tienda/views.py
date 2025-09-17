from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido, Cliente
from .forms import ProductoForm

def home(request):
    # render() recibe: request, ruta de template, contexto (diccionario)
    return render(request, "tienda/home.html", {})

def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})

def lista_pedidos(request):
    pedidos = Pedido.objects.select_related("cliente").prefetch_related("productos").order_by("-fecha")
    return render(request, "tienda/lista_pedidos.html", {"pedidos": pedidos})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related("cliente").prefetch_related("productos"), pk=pk)
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = cliente.pedidos.select_related("cliente").prefetch_related("productos"). order_by("-fecha")

    return render(request, "tienda/detalle_cliente.html", {"cliente": cliente, "pedidos": pedidos})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:lista_productos")
    else:
        form = ProductoForm()
    
    return render(request, "tienda/crear_producto.html", {"form": form})

def editar_producto(request, pk):
    # Obtenemos el producto o devolvemos 404 si no existe
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        # Vinculamos datos de POST y la instancia a editar
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()  # esto actualiza 'producto' en BD
            return redirect("tienda:detalle_producto", pk=producto.pk)
    else:
        # GET: mostramos el formulario precargado con datos del producto
        form = ProductoForm(instance=producto)

    return render(
        request, "tienda/editar_producto.html", {"form": form, "producto": producto}
    )

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("tienda:lista_productos")

    return render(request, "tienda/eliminar_producto.html", {"producto": producto})
