import flet as ft


def main(page: ft.Page):
    page.title = "Ransa Negocio"
    page.bgcolor = "#FFFFFF" 
    page.appbar = ft.AppBar(
        title=ft.Text("Ransa Negocio", color=ft.colors.WHITE),
        bgcolor="#1B5051",  # Fondo de la AppBar
        center_title=False,  # No centrar el título
        actions=[
            ft.TextButton(
                "Iniciar sesión",
                on_click=lambda _: print("Iniciar sesión"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE70,  # Color del texto del botón
                ),
            ),
            ft.TextButton(
                "Contactos",
                on_click=lambda _: print("Contactos"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE70,  # Color del texto del botón
                ),
            ),
            ft.TextButton(
                "Sobre nosotros",
                on_click=lambda _: print("Sobre nosotros"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE70,  # Color del texto del botón
                ),
            ),
        ],
    )
    st = ft.Stack(
            ft.Image(
                src="Imagene-de-mercado.png",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
    ),

    main_content= ft.Container(
        content=ft.Column(
            controls=[  # Usar el contenedor creado arriba
          # Añadir el nuevo contenedor
                ft.Container(
                    content=ft.Text(
                        "Camiones de carga a tu disposicióncon la flota camiones tipo carguero",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,  # Texto blanco para contraste
                    ),
                    padding=2,
                    bgcolor="#1B5051",  # Fondo del contenedor
                    border_radius=10,  # Esquinas redondeadas
                ),
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=20,
    )

    # Botón en la parte inferior derecha
    bottom_right_button= ft.Container(
        content=ft.ElevatedButton(
            "Saber más",
            on_click=lambda _: print("Saber más"),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor="#1B5051",  # Fondo del botón
                shape=ft.RoundedRectangleBorder(
                    radius=8),  # Esquinas redondeadas
            ),
        ),
        alignment=ft.alignment.bottom_right,  # Alinear a la parte inferior derecha
        padding=-25,  # Ajustar el padding según sea necesario
    )

    # Agregar contenido principal y botón a la página
    page.add(
        ft.Column(
            controls=[main_content, bottom_right_button],  # Añadir el botón
        )
    )


ft.app(target=main)