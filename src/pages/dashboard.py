import flet as ft
from flet_route import Params, Basket
import datetime
from src.components.page import generate_page
from src.Api.person import Person


class DashboardPage:
    def view(self, page:ft.page, params:Params, basket:Basket):
        person = Person(token=page.client_storage.get('token'))

        def render_buttons():
            person_id = page.client_storage.get('person_id')
            if person_id == 1:
                return [
                    ft.ElevatedButton(
                        "Пользователи",
                        adaptive=True,
                        content=ft.Row(
                            [
                                ft.Icon(name=ft.icons.INBOX_SHARP),
                                ft.Text("Пользователи"),
                            ],
                            tight=True,
                        ),
                    ),
                    ft.ElevatedButton("Настройки системы")
                ]
            elif person_id == 2:
                return [
                    ft.ElevatedButton("Просмотр профиля", ),
                    ft.ElevatedButton("Мои заказы", )]

        def transform_date(date):
            months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                      'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
            day,month, = date.split('.')
            return f'{day} {months[int(month) - 1]}'



        page.window.width = 1200
        page.window.height = 700
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window.resizable = True

        person_id = page.client_storage.get('person_id')


        name = None
        last_name = None

        try:
           result = person.find_person(person_id)

           if result['status'] == 200:
               name = result['body'].get("name")
               last_name = result['body'].get("last_name")
        except Exception as e:
            # password.error_text = f"Произошла ошибка: {str(e)}"
            page.update()

        greetings = ft.Text(
            f"Добро пожаловать, {name}!",
            color="orange",
            size=20,
            weight=ft.FontWeight.BOLD
        )
        today = ft.Text("Сегодня " + transform_date(datetime.datetime.today().strftime("%d.%m")),
                        size=18)
        users = ft.ElevatedButton(
            "Пользователи",
            adaptive=True,
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.INBOX_SHARP),
                    ft.Text("Пользователи"),
                ],
            ),
        )

        return ft.View(
            "/dashboard",
            controls = generate_page(
                page=page,
                controls=[
                    greetings,
                    today,
                    *render_buttons()
                ]
            )

        )