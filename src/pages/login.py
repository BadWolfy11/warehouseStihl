import flet as ft
from flet_route import Params, Basket


class LoginPage:
    def view(self, page:ft.page, params:Params, basket:Basket):
        def btn_click(txt_name: ft.TextField, password: ft.TextField):
            if not txt_name.value:
                txt_name.error_text = "Пожалуйста, введите логин"
                page.update()
            elif not password.value:
                password.error_text = "Пожалуйста, введите пароль"
                page.update()
            else:
                txt_name.error_text = None
                password.error_text = None
                page.update()
                login = txt_name.value
                passwd = password.value
                page.go('/dashboard')

        page.window.width = 1200
        page.window.height = 700
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window.resizable = False
        page.window.icon = 'src/assets/images/logo.png'

        txt_name = ft.TextField(label="Логин", filled=True, focused_color = "orange")
        password = ft.TextField(label="Пароль", password=True, can_reveal_password=True, filled = True, focused_color = "orange")
        btn = ft.ElevatedButton("Войти",
            color="orange",
            height=50,
            width=100,
            on_click = lambda x: btn_click(
                txt_name=txt_name,
                password=password
            )
        )

        forget_link = ft.Container(ft.Text('Забыли пароль?'))

        return ft.View(
            "/",
            controls=[
                ft.Row(
                    expand = True,
                    controls = [
                        ft.Container(
                            expand = 2,
                            padding = ft.padding.all(40),
                            content = ft.Column(
                                alignment = ft.MainAxisAlignment.CENTER,

                                controls= [
                                    ft.Text(
                                        'Добро пожаловать в систему STIHL',
                                        color = "orange",
                                        size = 25,
                                        weight = ft.FontWeight.NORMAL
                                    ),
                                    txt_name,
                                    password,
                                    btn

                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            content =
                            ft.Image(
                                src = 'src/assets/images/bg_login.jpg',
                                width = 1200,
                                height = 900,
                                fit = ft.ImageFit.COVER
                            )

                        )

                    ]
                )
            ],
        padding = 0
    )
