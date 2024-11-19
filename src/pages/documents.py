import flet as ft
from flet_route import Params, Basket

from src.components.bars.documents_bar import DocumentsBar
from src.components.page import generate_page
from src.components.generate_pdf import generate_pdf
from src.Api.documents import Documents



class DocumentsPage:
    def view(self, page: ft.page, params: Params, basket: Basket):
        name = ft.TextField(label="Название", filled=True, focused_color="orange")
        description = ft.TextField(label="Описание", filled=True,
                                   focused_color="orange")
        tasks_view = ft.Column()
        pagination = DocumentsBar(token=page.client_storage.get('token'), page=page, offset= 0)

        def add_clicked(e):
            tasks_view.controls.append(ft.Text(name.value))
            name.value = ""
            page.update()

        def generate_pdf_clicked(e):
            documents_api = Documents(token=page.client_storage.get('token'))
            documents_data = documents_api.all_document(page=1, itemsPerPage=100)

            pdf_buffer = generate_pdf(documents_data['body']['data'], documents_data['body']['total_count'])

            with open("documents.pdf", "wb") as f:
                f.write(pdf_buffer.read())
            page.launch_url("documents.pdf")

        pdf_button = ft.ElevatedButton("Сгенерировать PDF", on_click=generate_pdf_clicked)
        done = ft.ElevatedButton(
            "Сохранить",
             color="orange",
             height=50,
             width=150,
             on_click= add_clicked
        )

        txt_number = ft.TextField(value="0", text_align="right", width=100)
        add_btn = ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.ORANGE, on_click= lambda e: page.open(dlg))

        def close_dialog(e):
            dlg.open = False
            page.update()

        def minus_click(e):
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()

        def plus_click(e):
            txt_number.value = str(int(txt_number.value) + 1)
            page.update()

        dlg = ft.AlertDialog(
            title=ft.Text("Добавить новые документы"),
            content = ft.Column(
                controls=[
                    name,
                    description,
                    ft.Row(
                        [
                            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                            txt_number,
                            ft.IconButton(ft.icons.ADD, on_click=plus_click),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [   done,
                            ft.TextButton("Закрыть",
                                          height = 50,
                                          width = 150,
                                          on_click = close_dialog)
                            ]
                    ),

                ],


            )
        )

        return ft.View(
            "/documents",
            controls=generate_page(
                page=page,
                controls=[
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.Container(
                                expand=2,
                                padding=ft.padding.all(40),
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,

                                    controls=[
                                        ft.Text("Документы", size=24),
                                        ft.TextButton("Назад", on_click=lambda e: page.go("/dashboard")),
                                        pagination.panel,
                                        ft.Container(
                                            expand=4,
                                            alignment=ft.alignment.bottom_right,
                                            content=ft.Row([add_btn, pdf_button ]),
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )