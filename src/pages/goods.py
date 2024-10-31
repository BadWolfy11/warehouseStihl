import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page

class GoodsPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        return ft.View(
            "/goods",

            controls= generate_page(
                page=page,
                controls=[
                ft.Text("Товары", size=24),
                ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),

                ]

            )

        )
