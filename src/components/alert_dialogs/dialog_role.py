import flet as ft

from src.Api.role import Role


class RoleManager:
    def __init__(self, page: ft.Page, token: str, item_id: int | None = None):
        self.page = page
        self.role = Role(token)

        self.item_id = item_id
        self.name = ft.TextField(label="Название", filled=True, focused_color="orange")


        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Подтвердить"),
            content=ft.Text("Вы точно хотите удалить роль?"),
            actions=[
                ft.TextButton("Да", on_click=self.delete_item),
                ft.TextButton("Нет", on_click=self.close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss= self.close
        )

        self.dlg = ft.AlertDialog(
            title=ft.Text("Добавить новую роль" if self.item_id is None else "Изменить роль"),
            content=ft.Column([
                self.name,
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

    def delete_item(self, e):
        delete_item =self.role.delete_roles(id=self.item_id)
        if delete_item['status'] == 200:
            self.page.snack_bar = ft.SnackBar(ft.Text("Роль успешно удалена!"))
            self.page.snack_bar.open = True
            self.dlg_modal.open = False
            self.page.update()


    def open_delete(self, e):
        print(self.dlg_modal)
        self.dlg_modal.open = True

        self.page.update()

    def open(self, e):
        self.dlg.open = True

        if self.item_id is not None:
            self.load_item(self.item_id)

        self.page.update()

    def close(self, e):
        self.dlg.open = False
        self.page.update()

    def add(self, e):
        if not self.name.value:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Название должно быть заполнено.", color="red")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        result = self.role.new_roles(
            name=self.name.value,
        )

        if result['status'] == 200:
            self.page.snack_bar = ft.SnackBar(ft.Text("Роль успешно добавлена!"))
            self.page.snack_bar.open = True
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Ошибка: {result['body'].get('message', 'Неизвестная ошибка')}"))
            self.page.snack_bar.open = True

        self.clear_values()
        self.close(None)
        self.page.update()

    def load_item(self, item_id : int):
        find_item = self.role.find_roles(id=item_id)

        if find_item['status'] == 200:
            self.name.value = find_item['body']["name"]
        self.page.update()

    def save(self, e):
        update_role = self.role.update_roles(
            name=self.name.value
        )

        if update_role['status'] == 200:
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

