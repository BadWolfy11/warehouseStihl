import flet as ft
from flet_route import Routing, path
from src.pages.login import LoginPage
from src.pages.dashboard import DashboardPage
from src.pages.goods import GoodsPage
from src.pages.documents import DocumentsPage
from src.pages.expenses import ExpensesPage
from src.pages.income import IncomePage
from src.pages.outcome import OutcomePage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear = True, view = LoginPage().view),
            path(url='/dashboard', clear = False, view = DashboardPage().view),
            path(url='/goods', clear = False, view = GoodsPage().view),
            path(url='/documents', clear=False, view=DocumentsPage().view),
            path(url='/expenses', clear=False, view=ExpensesPage().view),
            path(url='/income', clear=False, view=IncomePage().view),
            path(url='/outcome', clear=False, view=OutcomePage().view)

        ]

        Routing(
            page=self.page,
            app_routes = self.app_routes
        )
        self.page.go(self.page.route)
