import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page
from src.components.bars.roles_bar import RolesBar
from src.components.alert_dialogs.dialog_role import RoleManager

class ExpenseCategoriesPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        pagination = RolesBar(token=page.client_storage.get('token'), page=page, per_page=10)
        role = RoleManager(token=page.client_storage.get('token'), page = page, )

        return ft.View(
            "/expense_categories",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Text("Виды завтрат", size=24),
                    ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
                    pagination.list_view,
                    pagination.bar,
                    role.dlg,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD,
                        bgcolor=ft.colors.ORANGE,
                        on_click=product.open
                    ),
                ]
            )
        )
