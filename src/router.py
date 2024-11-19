import flet as ft
from flet_route import Routing, path
from src.pages.login import LoginPage
from src.pages.dashboard import DashboardPage
from src.pages.goods import GoodsPage
from src.pages.documents import DocumentsPage
from src.pages.expenses import ExpensesPage
from src.pages.role import RolePage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear = True, view = LoginPage().view),
            path(url='/dashboard', clear = False, view = DashboardPage().view),
            path(url='/goods', clear = False, view = GoodsPage().view),
            path(url='/documents', clear=False, view=DocumentsPage().view),
            path(url='/expenses', clear=False, view=ExpensesPage().view),
            path(url='/role', clear=False, view=RolePage().view),
            path(url='/users', clear=False, view=ExpensesPage().view),
            path(url='/expense_categories', clear=False, view=ExpensesPage().view),

        ]

        Routing(
            page=self.page,
            app_routes = self.app_routes
        )
        self.page.go(self.page.route)
