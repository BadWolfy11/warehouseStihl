import flet as ft

from src.Api.categories import Categories
from src.Api.goods import Goods


class ProductManager:
    def __init__(self, page: ft.Page, token: str, item_id: int | None = None):
        self.page = page
        self.API_categories = Categories(token)
        self.goods = Goods(token)

        self.item_id = item_id
        self.name = ft.TextField(label="Название", filled=True, focused_color="orange")
        self.description = ft.TextField(label="Описание", filled=True, focused_color="orange")
        self.barcode = ft.TextField(label="штрихкод", filled=True, focused_color="orange")
        self.attachments = ft.TextField(label="Дополнительно", filled=True, focused_color="orange")

        self.category_id = ft.Dropdown(
            label="Категории",
            hint_text="выберите категорию товара",
            autofocus=True,
        )

        self.dlg = ft.AlertDialog(
            title=ft.Text("Добавить новый товар" if self.item_id is None else "Изменить товар"),
            content=ft.Column([
                self.name,
                self.description,
                self.barcode,
                self.category_id,
                self.attachments,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Сохранить",
                            color="orange",
                            height=50,
                            width=150,
                            on_click=self.add if self.item_id is None else self.save
                        ),
                        ft.TextButton(
                            "Закрыть", height=50, width=150, on_click=self.close
                        ),
                    ]
                ),
            ])
        )

    def load_categories(self, e):
        try:
            offset, limit = 0, 100
            categories = []

            while True:
                response = self.API_categories.all_categories(offset, limit)

                if response['status'] == 200 and not "error" in response:
                    items = response['body'].get("data", {})
                    categories += items
                    if response['body'].get("total_count", 0) > (offset + limit):
                        offset += limit
                        continue
                    break
                else:
                    self.page.snack_bar = ft.SnackBar(
                        content=ft.Text("Ошибка при загрузке категорий.", color="red")
                    )
                    self.page.snack_bar.open = True

            self.category_id.options = [
                ft.dropdown.Option(text=category["name"], key=category["id"])
                for category in categories
            ]

            self.page.update()
        except Exception as e:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Произошла ошибка: {str(e)}", color="red")
            )
            self.page.snack_bar.open = True
            self.page.update()

    def open(self, e):
        self.dlg.open = True
        self.load_categories(e)

        if self.item_id is not None:
            self.load_item(self.item_id)

        self.page.update()

    def close(self, e):
        self.dlg.open = False
        self.page.update()

    def add(self, e):
        if not self.name.value or not self.description.value:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Название и описание не должны быть пустыми.", color="red")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        result = self.goods.new_goods(
            barcode=self.barcode.value,
            name=self.name.value,
            description=self.description.value,
            category_id=int(self.category_id.value),
            attachments=self.attachments.value
        )

        if result['status'] == 200:
            self.page.snack_bar = ft.SnackBar(ft.Text("Товар успешно добавлен!"))
            self.page.snack_bar.open = True
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Ошибка: {result['body'].get('message', 'Неизвестная ошибка')}"))
            self.page.snack_bar.open = True

        self.clear_values()
        self.close(None)
        self.page.update()

    def load_item(self, item_id : int):
        find_item = self.goods.find_good(id=item_id)

        if find_item['status'] == 200:
            self.name.value = find_item['body']["name"]
            self.description.value = find_item['body']["description"]
            self.barcode.value = find_item['body']["barcode"]
            self.category_id.value = str(find_item['body']["category_id"])
            self.attachments.value = find_item['body']["attachments"]

        self.page.update()

    def save(self, e):
        update_good = self.goods.update_good(
            id=self.item_id,
            name=self.name.value,
            description=self.description.value,
            barcode=self.barcode.value,
            category_id=self.category_id.value,
            attachments=self.attachments.value
        )

        if update_good['status'] == 200:
            self.page.snack_bar = ft.SnackBar(ft.Text("Товар успешно обновлен!"))
            self.page.snack_bar.open = True
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Ошибка"))
            self.page.snack_bar.open = True

        self.clear_values()
        self.close(None)
        self.page.update()

    def clear_values(self):
        self.name.value = ""
        self.description.value = ""
        self.barcode.value = ""
        self.category_id.value = None
        self.attachments.value = ""

