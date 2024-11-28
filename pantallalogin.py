import flet as ft

def main(page: ft.Page):
    page.title = "Login - Ransa Negocio"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#000000"  # Fondo negro

    # Contenido del login
    login_content = ft.Container(
        width=300,
        padding=20,
        decoration=ft.BoxDecoration(
            color="#1B5051",  # Fondo del contenedor
            border_radius=10,
        ),
        content=ft.Column(
            controls=[
                ft.Text(
                    "Hola buenos días le saluda la empresa 'Ransa'",
                    size=16,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.TextField(
                    label="Correo:",
                    filled=True,
                    fill_color=ft.colors.GRAY_300,
                ),
                ft.TextField(
                    label="Contraseña:",
                    filled=True,
                    fill_color=ft.colors.GRAY_300,
                    password=True,
                ),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            text="Registrarse",
                            on_click=lambda _: print("Registrarse"),
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE
                            ),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.ElevatedButton(
                    text="Iniciar sesión",
                    on_click=lambda _: print("Iniciar sesión"),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLACK,
                        padding=ft.Padding(horizontal=50, vertical=15),
                    ),
                ),
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    # Agregar el contenido de login a la página
    page.add(ft.Container(
        content=login_content,
        alignment=ft.Alignment.CENTER,
    ))

ft.app(target=main)
