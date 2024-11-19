import flet as ft
from src.Api.goods import Goods
from src.Api.expenses import Expenses
from src.Api.goods_documents import GoodsDocuments
from src.Api.role import Role
from src.Api.expense_categories import ExpenseCategories
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

def fetch_all_documents_expenses(token: str, limit: int = 100, offset: int = 0) -> dict:
    documents_expenses = GoodsDocuments(token)
    response = documents_expenses.all_expenses(limit= limit, offset= offset)

    if response['status'] == 200:

        data = response['body']
        return {
            "documents": data.get("documents", []),
            "total": data.get("total", 0)
        }
    else:
        return {
            "error": response['body'].get("Ошибка", "Ой у вас пропали товары"),
        }


def fetch_paginated_role(token: str, page: int, items_per_page: int) -> dict:
    role_api = Role(token)
    response = role_api.all_roles(page=page, itemsPerPage=items_per_page)

    if response['status'] == 200:
        return {
            "items": response['body'].get("data", {}),
            "total_pages": math.ceil(
                response['body'].get("total_count", 0) / response['body'].get("items_per_page", 1)
            ),
        }
    else:
        return {
            "error": response['body'].get("Ошибка", "Ой у вас пропали роли"),
        }

def fetch_paginated_expense_categories(token: str, page: int, items_per_page: int) -> dict:
    expense_categories_api = ExpenseCategories(token)
    response = expense_categories_api.all_exp_categories(page=page, itemsPerPage=items_per_page)

    if response['status'] == 200:
        return {
            "items": response['body'].get("data", {}),
            "total_pages": math.ceil(
                response['body'].get("total_count", 0) / response['body'].get("items_per_page", 1)
            ),
        }
    else:
        return {
            "error": response['body'].get("Ошибка", "Ой у вас пропали Виды затрат"),
        }