import flet as ft

def main(page: ft.Page):
    page.title = "Splash Screen"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1B5051"  # Fondo del splash screen con el color verde oscuro

    # Contenido del splash screen
    splash_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Ransa Negocio E.I.R.L.",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ),
                ft.Image(src="assets/warehouse.jpg", width=300, height=200),
                ft.Text(
                    "Impulsa tu negocio con nosotros",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ),
                ft.Image(src="assets/port.jpg", width=300, height=200),
                ft.Image(src="assets/truck.jpg", width=300, height=200),
                ft.ElevatedButton(
                    "Ingresar",
                    on_click=lambda _: print("Navegando a la siguiente pantalla..."),
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
        alignment=ft.Alignment.CENTER,
        padding=20,
    )

    # Agregar el contenido del splash screen a la página
    page.add(splash_content)

ft.app(target=main)
