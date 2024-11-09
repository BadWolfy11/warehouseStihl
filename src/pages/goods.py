import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page
from src.components.paginated_bar import PaginatedBar

class GoodsPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        pagination = PaginatedBar(token=page.client_storage.get('token'), page=page, per_page=10)

        return ft.View(
            "/goods",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Text("Товары", size=24),
                    ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
                    pagination.list_view,
                    pagination.bar
                ]
            )
        )
