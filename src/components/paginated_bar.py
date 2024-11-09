import flet as ft
from src.components.info_data import fetch_paginated_goods


class PaginatedBar:
    def __init__(self, token: str, page: ft.Page, per_page: int = 10):
        self.token = token
        self.page = page
        self.per_page = per_page

        self.current_page = 1
        self.total_pages = 1

        self.list_view = ft.ListView(expand=True, spacing=10, padding=10)
        self.bar = ft.Row(
            controls=[ ft.Text(f"Страница {self.current_page} из {self.total_pages}") ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.load_goods(self.current_page)

    def previous_page(self, e):
        if self.current_page > 1:
            self.load_goods(self.current_page - 1)

    def next_page(self, e):
        if self.current_page < self.total_pages:
            self.load_goods(self.current_page + 1)

    def load_goods(self, current_page: int):
        result = fetch_paginated_goods(self.token, current_page, self.per_page)

        if "error" in result:
            self.list_view.controls = [ft.Text(result["error"], color=ft.colors.RED)]
        elif result["total_pages"] < current_page:
            # self.list_view.controls = ["Данные были обновлены, необходима перезагрузка страницы", color=ft.colors.RED)]
            pass
        else:
            self.current_page: int = current_page

            self.total_pages: int = result["total_pages"]

            self.list_view.controls = []

            for item in result["items"]:
                self.list_view.controls.append(ft.ListTile(title=ft.Text(f"{item['id']} - {item['name']}")))

        self.update_bar()

        self.page.update()

    def update_bar(self):

        controls = []
        if self.current_page > 1:
            controls.append(ft.ElevatedButton("Назад", on_click=self.previous_page))

        controls.append(ft.Text(f"Страница {self.current_page} из {self.total_pages}"))

        if self.total_pages > self.current_page:
            controls.append(ft.ElevatedButton("Вперёд", on_click=self.next_page))

        self.bar.controls = controls
