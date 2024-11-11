import flet as ft
from src.Api.goods import Goods
from src.Api.expenses import Expenses
import math


def fetch_paginated_goods(token: str, page: int, items_per_page: int) -> dict:
    goods_api = Goods(token)
    response = goods_api.all_goods(page=page, itemsPerPage=items_per_page)

    if response['status'] == 200:
        return {
            "items": response['body'].get("data", {}),
            "total_pages": math.ceil(
                response['body'].get("total_count", 0) / response['body'].get("items_per_page", 1)
            ),
        }
    else:
        return {
            "error": response['body'].get("Ошибка", "Ой у вас пропали товары"),
        }


def fetch_paginated_expenses(token: str, page: int, items_per_page: int) -> dict:
    expenses_api = Expenses(token)
    response = expenses_api.all_expenses(page=page, itemsPerPage=items_per_page)

    if response['status'] == 200:
        return {
            "items": response['body'].get("data", {}),
            "total_pages": math.ceil(
                response['body'].get("total_count", 0) / response['body'].get("items_per_page", 1)
            ),
        }
    else:
        return {
            "error": response['body'].get("Ошибка", "Ой у вас пропали товары"),
        }

