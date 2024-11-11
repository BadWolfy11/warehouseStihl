import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page
from src.components.bars.expenses_bar import PaginatedBar

class ExpensesPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        pagination = PaginatedBar(token=page.client_storage.get('token'), page=page, per_page=10)
        return ft.View(
            "/expenses",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Text("Прочие затраты", size=24),
                    ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
                    pagination.list_view,
                    pagination.bar,
            ]
            )
        )