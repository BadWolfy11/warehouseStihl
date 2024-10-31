import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page

class ExpensesPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        return ft.View(
            "/expenses",
            controls=generate_page(
                page=page,
                controls=[
                ft.Text("Прочие затраты", size=24),
                ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
            ]
            )
        )