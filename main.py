import flet as ft
from fletcarousel import BasicHorizontalCarousel  # Asegúrate de tener este paquete instalado

def main(page: ft.Page):
    page.title = "Tienda de Productos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    # Lista de datos con nombre, precio e imagen
    productos = [
        {"nombre": "Producto 1", "precio": 10.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 2", "precio": 20.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 3", "precio": 30.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 4", "precio": 40.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 5", "precio": 50.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 6", "precio": 60.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 7", "precio": 70.0, "imagen": "https://via.placeholder.com/150"},
        {"nombre": "Producto 8", "precio": 80.0, "imagen": "https://via.placeholder.com/150"}
    ]

    categorias = ["Electrónica", "Ropa", "Hogar", "Juguetes", "Deportes", "Libros"]

    carrusel_imagenes = [
        "https://via.placeholder.com/800x300",
        "https://via.placeholder.com/800x300",
        "https://via.placeholder.com/800x300"
    ]

    # Función para mostrar detalles del producto en una pantalla emergente
    def mostrar_detalle_producto(producto):
        def agregar_cantidad(e):
            cantidad_label.value = str(int(cantidad_label.value) + 1)
            cantidad_label.update()
        
        def reducir_cantidad(e):
            cantidad_label.value = str(max(1, int(cantidad_label.value) - 1))
            cantidad_label.update()

        cantidad_label = ft.Text("1", size=16)
        
        page.dialog = ft.AlertDialog(
            title=ft.Text("Detalles del Producto"),
            content=ft.Column([
                ft.Text(producto["nombre"], size=24, weight="bold"),
                ft.Text(f"Precio: ${producto['precio']}", size=20),
                ft.Row([
                    ft.IconButton(ft.icons.REMOVE, on_click=reducir_cantidad),
                    cantidad_label,
                    ft.IconButton(ft.icons.ADD, on_click=agregar_cantidad)
                ])
            ]),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog.open = True
        page.update()

    # Función para crear una tarjeta de vista (CardView)
    def crear_card(producto):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Image(src=producto["imagen"], width=150, height=150),
                    ft.Text(producto["nombre"], size=20, weight="bold"),
                    ft.Text(f"Precio: ${producto['precio']}", size=16)
                ], alignment="center"),
                padding=10,
                alignment=ft.alignment.center,
                on_click=lambda e: mostrar_detalle_producto(producto)  # Evento de clic agregado aquí
            ),
            elevation=5,
            margin=5
        )

    # Crear una lista de filas, cada una conteniendo 4 tarjetas de vista
    filas = []
    for i in range(0, len(productos), 4):
        fila = ft.Row(controls=[crear_card(producto) for producto in productos[i:i + 4]], alignment="center")
        filas.append(fila)

    # Crear carrusel de imágenes usando BasicHorizontalCarousel
    carrusel = BasicHorizontalCarousel(
        page=page,
        items_count=3,
        items=[
            ft.Container(
                content=ft.Image(src=img),
                height=200,
                width=300,
                bgcolor='red',
                border_radius=15,
                alignment=ft.alignment.center,
            ) for img in carrusel_imagenes
        ],
        buttons=[
            ft.FloatingActionButton(
                icon=ft.icons.NAVIGATE_BEFORE,
                bgcolor='#1f2127'
            ),
            ft.FloatingActionButton(
                icon=ft.icons.NAVIGATE_NEXT,
                bgcolor='#1f2127'
            )
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        items_alignment=ft.MainAxisAlignment.CENTER
    )

    # Crear sección de categorías
    categorias_row = ft.Row(
        controls=[
            ft.Chip(label=categoria) for categoria in categorias
        ],
        scroll="auto",
        spacing=10
    )

    # Barra inferior de navegación
    barra_inferior = ft.NavigationBar(
        items=[
            ft.NavigationBarItem(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarItem(icon=ft.icons.SEARCH, label="Buscar"),
            ft.NavigationBarItem(icon=ft.icons.SHOPPING_CART, label="Carrito"),
            ft.NavigationBarItem(icon=ft.icons.ACCOUNT_CIRCLE, label="Perfil"),
        ],
        selected_index=0
    )

    # Agregar elementos al layout de la página
    page.add(
        ft.Column(
            controls=[
                carrusel,
                ft.Text("Categorías", size=24, weight="bold", padding=10),
                categorias_row,
                ft.Text("Productos", size=24, weight="bold", padding=10),
                ft.Column(controls=filas, alignment="center")
            ],
            scroll="adaptive"
        ),
        barra_inferior
    )

ft.app(target=main)
