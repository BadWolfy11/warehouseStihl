import flet as ft
from flet_route import Params, Basket
import datetime
from src.components.page import generate_page

class DashboardPage:
    def view(self, page:ft.page, params:Params, basket:Basket):
        def transform_date(date):
            months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                      'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
            day,month, = date.split('.')
            return f'{day} {months[int(month) - 1]}'
        page.window.width = 1200
        page.window.height = 700
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window.resizable = True

        style_menu = ft.ButtonStyle(color = {ft.ControlState.HOVERED: ft.colors.WHITE},
                                    icon_size = 14)

        greetings = ft.Text("Добро пожаловать, USER",
                            color="orange",
                            size=20,
                            weight=ft.FontWeight.BOLD
                            )
        today = ft.Text("Сегодня " + transform_date(datetime.datetime.today().strftime("%d.%m")),
                        size=18)
        goods = ft.ElevatedButton(
            "Товары",
            width = 150,
            height= 100,
            adaptive=True,
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.INBOX_SHARP),
                    ft.Text("Товары"),
                ],
                tight=True,
            ),
        )

        return ft.View(
            "/dashboard",
            controls = generate_page(
                page=page,
                controls=[
                    greetings,
                    today,
                    goods
                ]
            )

        )