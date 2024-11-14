import flet as ft
from flet_route import Params, Basket

from src.components.alert_dialogs.dialog_expenses import ExpensesManager
from src.components.page import generate_page
from src.components.bars.expenses_bar import ExpensePaginatedBar

class ExpensesPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        pagination = ExpensePaginatedBar(token=page.client_storage.get('token'), page=page, per_page=10)
        expense = ExpensesManager(token=page.client_storage.get('token'), page=page, )
        return ft.View(
            "/expenses",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Text("Прочие затраты", size=24),
                    ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
                    pagination.list_view,
                    pagination.bar,
                    expense.dlg,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD,
                        bgcolor=ft.colors.ORANGE,
                        on_click=expense.open
                    ),
            ]
            )
        )