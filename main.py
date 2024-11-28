import flet as ft

def main(page: ft.Page):
    page.title = "Ransa Negocio"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor ="#1B5051" # Color de fondo de la página

    # Crear el menú de navegación
    app_bar=ft.AppBar(
        title=ft.Text("Ransa Negocio"),
        bgcolor="#1B5051",
        actions=[
            ft.TextButton("Iniciar sesión", on_click=lambda _: print("Iniciar sesión"), height=50, padding=ft.Padding(20)),
            ft.TextButton("Contactos", on_click=lambda _: print("Contactos"), height=50, padding=ft.Padding(20)),
            ft.TextButton("Sobre nosotros", on_click=lambda _: print("Sobre nosotros"), height=50, padding=ft.Padding(20)),
        ],
    )
    nav_menu = ft.Row(
        controls=[
            ft.TextButton("Iniciar sesión", on_click=lambda _: print("Iniciar sesión")),
            ft.TextButton("Contactos", on_click=lambda _: print("Contactos")),
            ft.TextButton("Sobre nosotros", on_click=lambda _: print("Sobre nosotros")),
        ],
        alignment=ft.MainAxisAlignment.END
    )

    # Crear contenedores con estilos manuales
    left_container = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="Imagene-de-mercado.png", width=200, height=200),
                ft.Text("Acuerdos comerciales y financieros", weight=ft.FontWeight.NORMAL),
            ]
        ),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=2)
    )

    right_container = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="assets/imagenen-de-camion.png", width=200, height=200),
                ft.Text("Servicio de transporte de mercancías", weight=ft.FontWeight.NORMAL),
            ]
        ),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=2)
    )

    # Crear contenido principal
    main_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "Camiones de carga a tu disposición con la flota camiones tipo carguero",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.DEEP_PURPLE
                    ),
                    padding=20
                ),
                ft.Row(
                    controls=[left_container, right_container],
                    spacing=20
                ),
                ft.ElevatedButton(
                    "Saber más",
                    on_click=lambda _: print("Saber más"),
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.DEEP_PURPLE
                    )
                )
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=20,
        bgcolor=ft.colors.LIGHT_BLUE_50  # Color de fondo para el contenido principal
    )

    # Añadir al layout de la página
    page.add(
        ft.Column(
            controls=[
                nav_menu,
                main_content,
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True,
        )
    )

ft.app(target=main)


