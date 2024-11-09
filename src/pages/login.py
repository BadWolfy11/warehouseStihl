import flet as ft
import requests
from flet_route import Params, Basket
from src.Api.auth import Auth
import asyncio

class LoginPage:
    def __init__(self):
        self.person_id = None
        self.token = None

    def get_person(self):
        return self.person_id

    def get_token(self):
        return self.token

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
                auth_client = Auth(token="")

                try:
                    result = auth_client.login(
                        login=txt_name.value,
                        password=password.value
                    )

                    if result['status'] == 200:
                        page.client_storage.set('user_id', result['body'].get("user_id"))
                        page.client_storage.set('person_id', result['body'].get("person_id"))
                        page.client_storage.set('role_id', result['body'].get("role_id"))
                        page.client_storage.set('login', result['body'].get("login"))
                        page.client_storage.set('token', result['body'].get("access_token"))

                        page.go('/dashboard')
                    else:
                        password.error_text = result['body'].get("detail", "Ошибка")
                        page.update()

                except Exception as e:
                    # Handle unexpected exceptions, e.g., network issues, server errors, etc.
                    password.error_text = f"Произошла ошибка: {str(e)}"
                    page.update()

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
