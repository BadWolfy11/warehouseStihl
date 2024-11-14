import datetime
import flet as ft

from src.Api.expense_categories import ExpenseCategories
from src.Api.expenses import Expenses


class ExpensesManager:
    def __init__(self, page: ft.Page, token: str, item_id: int | None = None):
        self.page = page
        self.API_expense_categories = ExpenseCategories(token)
        self.expenses = Expenses(token)
        self.info = datetime.datetime.now().strftime('%Y-%m-%d')
        self.item_id = item_id
        self.name = ft.TextField(label="Название", filled=True, focused_color="orange")
        self.amount = ft.TextField(label="стоимость", filled=True, focused_color="orange")
        self.data = ft.TextField(label="выбранная дата", filled=True, focused_color="orange")

        self.date_btn =  ft.ElevatedButton(
            "Выберите дату",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: self.page.open(
                self.date_picker
            ),
        )
        self.date_picker = ft.DatePicker(
            first_date=datetime.datetime(year=2023, month=10, day=1),
            last_date=datetime.datetime(year=2024, month=10, day=1),
            on_change=self.date_changed
        )
        # self.selected_date = self.date_picker.value.strftime('%Y-%m-%d')
        self.attachments = ft.TextField(label="Дополнительно", filled=True, focused_color="orange")

        self.category_id = ft.Dropdown(
            label="Категории",
            hint_text="выберите категорию товара",
            autofocus=True,
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Подтвердить"),
            content=ft.Text("Вы точно хотите удалить расходы??"),
            actions=[
                ft.TextButton("Да", on_click=self.delete_item),
                ft.TextButton("Нет", on_click=self.close_delete),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss= self.close_delete
        )

        self.dlg = ft.AlertDialog(
            title=ft.Text("Добавить новые расходы" if self.item_id is None else "Изменить расходы"),
            content=ft.Column([
                self.name,
                self.amount,
                self.data,
                self.date_btn,
                self.date_picker,
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

    def delete_item(self, e):
        delete_item =self.expenses.delete_expenses(id=self.item_id)
        if delete_item['status'] == 200:
            self.page.snack_bar = ft.SnackBar(ft.Text("Расходы успешно удалены!"))
            self.page.snack_bar.open = True
            self.dlg_modal.open = False
            self.page.update()

    def date_changed(self, e):
        if e.data:
            self.data.value = f"Выбранная дата: {self.date_picker.value.strftime('%Y-%m-%d')}"
            self.info = self.date_picker.value.strftime('%Y-%m-%d')
            self.page.update()

    # .strftime()
    def load_categories(self, e):
        try:
            offset, limit = 0, 100
            categories = []

            while True:
                response = self.API_expense_categories.all_expense_categories(offset, limit)

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


    def open_delete(self, e):
        print(f'Open delete debug: {self.dlg_modal}')
        self.dlg_modal.open = True

        self.page.update()

    def open(self, e):
        self.dlg.open = True
        self.load_categories(e)

        if self.item_id is not None:
            self.load_item(self.item_id)

        self.page.update()

    def close(self, e):
        print(e)
        self.dlg.open = False
        self.page.update()

    def close_delete(self, e):
        self.dlg_modal.open = False
        self.page.update()

    def add(self, e):
        # if not self.name.value or not self.amount.value or not self.info or not self.category_id.value:
        #     self.page.snack_bar = ft.SnackBar(
        #         content=ft.Text("Название, описание, дата и категория не должны быть пустыми.", color="red")
        #     )
        #     self.page.snack_bar.open = True
        #     self.page.update()
        #     return

        result = self.expenses.new_expenses(
            amount=int(self.amount.value) or 0,
            name=self.name.value,
            data=self.info,
            expense_category_id=int(self.category_id.value),
            attachments=self.attachments.value
        )

        print(f'Result of add: {result}')

        if result['status'] == 200:
            self.clear_values()
            self.close(None)

            self.page.snack_bar = ft.SnackBar(ft.Text("Расходы успешно добавлены!"))
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Ошибка: {result['body'].get('message', 'Неизвестная ошибка')}"))

        self.page.snack_bar.open = True
        # self.page.update()

    def load_item(self, item_id : int):
        find_item = self.expenses.find_expenses(id=item_id)

        if find_item['status'] == 200:
            self.name.value = find_item['body']["name"]
            self.amount.value = find_item['body']["amount"]
            self.data.value = find_item['body']["data"]
            self.category_id.value = str(find_item['body']["expense_category_id"])
            self.attachments.value = find_item['body']["attachments"]
            print(f'Load Item debug (expenses): {type(find_item['body']["data"])}')


        self.page.update()

    def save(self, e):
        update_good = self.expenses.update_expenses(
            id=self.item_id,
            name=self.name.value,
            amount=int(self.amount.value) or 0,
            data=self.info,
            expense_category_id=self.category_id.value,
            attachments=self.attachments.value

        )

        if update_good['status'] == 200:
            self.page.snack_bar = ft.SnackBar(ft.Text("Расходы успешно обновлены!"))
            self.page.snack_bar.open = True
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Ошибка"))
            self.page.snack_bar.open = True

        self.clear_values()
        self.close(None)
        self.page.update()

    def clear_values(self):
        self.name.value = ""
        self.amount.value = ""
        self.info = datetime.datetime.now().strftime('%Y-%m-%d')
        self.category_id.value = None
        self.attachments.value = ""

        # self.name,
        # self.amount,
        # self.data,
        # self.date_picker,
        # self.attachments,
        # self.category_id,

