import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page
from src.components.bars.paginated_bar import PaginatedBar
from src.components.alert_dialogs.dialog_goods import ProductManager

class GoodsPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        pagination = PaginatedBar(token=page.client_storage.get('token'), page=page, per_page=10)
        product = ProductManager(token=page.client_storage.get('token'), page = page, )

        return ft.View(
            "/goods",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Text("Товары", size=24),
                    ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
                    pagination.list_view,
                    pagination.bar,
                    product.dlg,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD,
                        bgcolor=ft.colors.ORANGE,
                        on_click=product.open
                    ),
                ]
            )
        )
