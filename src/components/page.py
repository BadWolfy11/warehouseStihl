from .sidebar import generate_sidebar

import flet as ft

def generate_page(page: ft.Page, controls: dict):
    return [
        ft.Row(
            expand = True,
            controls = [
                generate_sidebar(page=page),
                ft.Container(
                    expand=4,
                    padding = ft.padding.symmetric(15,10),
                    content=ft.Column(controls=controls)
                )
            ]
        )
    ]
