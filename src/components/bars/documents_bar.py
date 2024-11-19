import flet as ft
from src.components.info_data import fetch_all_documents_expenses
from src.components.alert_dialogs.dialog_goods import ProductManager


class DocumentsBar:
    def __init__(self, token: str, page: ft.Page, offset: int = 100):
        self.token = token
        self.page = page
        self.offset = offset

        self.current_items = None # limit
        self.total_pages = 1
        self.panel = ft.ExpansionPanelList(
            expand_icon_color=ft.colors.AMBER,
            elevation=8,
            divider_color=ft.colors.AMBER,
            controls=[]
        )

        self.load_goods()

    def load_goods(self, limit: int = 100):
        result = fetch_all_documents_expenses(self.token, limit, self.offset)

        if "error" in result:
            self.panel.controls.append(ft.Text(result["error"], color=ft.colors.RED))
            return

        self.current_items = len(result['documents'])
        self.total_pages = result["total"]
        self.panel.controls.clear()

        for doc in result["documents"]:
            items_list = []

            for item in doc["items"]:
                items_list.append(ft.ListTile(
                    title=ft.Text(item['name']),
                    subtitle=ft.Text(f"Quantity: {item['quantity']}"),
                    trailing=ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        tooltip="Delete item",
                        # on_click=lambda _: self.delete_item(doc_id=doc['id'], item_id=item['id'])
                    )
                ))

            exp_panel = ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"Document ID: {doc['id']} - {doc['name']} ({doc['date']})")),
                content=ft.Column(controls=items_list),
            )

            self.panel.controls.append(exp_panel)
        print("1")
        self.page.update()
