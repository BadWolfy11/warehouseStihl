import flet as ft
from flet_route import Params, Basket
from src.components.page import generate_page
from src.components.bars.expense_categories_bar import ExpenseCategoriesBar
from src.components.alert_dialogs.dialog_expense_categories import ExpenseDocumentsManager

class RolePage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        pagination = ExpenseCategoriesBar(token=page.client_storage.get('token'), page=page, per_page=10)
        role = ExpenseDocumentsManager(token=page.client_storage.get('token'), page = page,)

        return ft.View(
            "/role",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Text("Роли", size=24),
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
