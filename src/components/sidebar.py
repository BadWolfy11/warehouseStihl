import flet as ft

style_menu = ft.ButtonStyle(
    color = {ft.ControlState.HOVERED: ft.colors.WHITE},
    icon_size = 14
)

logotupe = ft.Container (
    padding = ft.padding.symmetric(17,13),
    content = ft.Row(
        controls = [
            ft.Image(
                src = 'src/assets/images/logo.png',
                width = 100,
                height = 50,
                fit = ft.ImageFit.FILL
            ),
            ft.Text(
                'STIHL Учет магазина',
                expand = True,
                color = "orange",
                size = 20
            )
        ],
        alignment = ft.MainAxisAlignment.START,
        spacing = 5,
        vertical_alignment = ft.CrossAxisAlignment.CENTER
    )
)

def generate_sidebar(page: ft.page):
    sidebar_menu = ft.Container(
        padding = ft.padding.symmetric(0,13),
        content = ft.Column(
            controls = [
                ft.Text('Меню', size = 18),
                ft.TextButton(
                    'Главная',
                    icon = 'HOME_ROUNDED',
                    style=style_menu,
                    on_click=lambda e: page.go("/dashboard"),
                ),
                ft.TextButton(
                    'Товары',
                    icon = 'PRODUCTION_QUANTITY_LIMITS',
                    style=style_menu,
                    on_click=lambda e: page.go("/goods"),
                ),
                ft.TextButton(
                    'Документы',
                    icon='EDIT_DOCUMENT',
                    style = style_menu,
                    on_click=lambda e: page.go("/documents")
                ),
                ft.TextButton(
                    'Остальные затраты',
                    icon='CALL_MISSED_OUTGOING',
                    style=style_menu,
                    on_click=lambda e: page.go("/expenses")
                ),
            ]

        )
    )

    return ft.Container(
        expand = 1,
        content = ft.Column(controls = [ logotupe, sidebar_menu, ft.Container(alignment=ft.alignment.bottom_left, padding = ft.padding.symmetric(0,13), content = ft.OutlinedButton(text="Выйти из аккаунта", on_click = lambda e: page.go("/")))])
    )
