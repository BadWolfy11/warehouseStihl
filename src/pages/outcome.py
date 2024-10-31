import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page


class OutcomePage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        return ft.View(
            "/outcome",

            controls=generate_page(
                page=page,
                    controls=[
                        ft.Text("Продажи", size=24),
                        ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),

                    ]

            )
        )
