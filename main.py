import flet as ft
from src.router import Router

def main(page: ft.Page):
    Router(page)

if __name__ == "__main__":
    ft.app(target=main, assets_dir ="assets")


# def main(page):
#     def show_snack_bar(msg):
#         snack_bar = SnackBar(content=Text(msg), bgcolor=colors.RED)
#         page.snack_bar = snack_bar
#         snack_bar.open = True
#
#     def btn_click(e):
#         if not txt_name.value:
#             txt_name.error_text = "Пожалуйста, введите логин"
#             page.update()
#         elif not password.value:
#             password.error_text = "Пожалуйста, введите пароль"
#             page.update()
#         else:
#             login = txt_name.value
#             passwd = password.value
#
#
#
#     page.window.width = 400
#     page.window.height = 500
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.window.resizable = False
#     txt_name = ft.TextField(label="Логин")
#     password = ft.TextField(label="Пароль", password=True, can_reveal_password=True)
#
#
#     page.add(txt_name, password, ft.ElevatedButton("Войти", on_click=btn_click))
#
#     page.update()
#
# ft.app(main)