from datetime import date

from .API import API, RequestMethod

class Expenses(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def all_expenses(self, page: int, itemsPerPage: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/expenses/get_paginated',
            params={
                'page': page,
                'itemsPerPage': itemsPerPage
            }
        )

    def new_expenses(self, data: str, amount: int, name: str,
                        attachments: str,
                        expense_category_id: int) -> dict:
        return self.request(
            method=RequestMethod.POST,
            path='/api/expenses/create',
            json={
                'data': data,
                'amount': amount,
                'name': name,
                'attachments': attachments,
                'expense_category_id': expense_category_id,
            }
        )

    def find_expenses(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path=f'/api/expenses/get/{id}',
        )

    def update_expenses(self, id: int, data: str | None = None, amount: int | None = None, name: str | None = None,
                        attachments: str | None = None,
                        expense_category_id: int | None = None) -> dict:

        print(data)
        return self.request(
            method=RequestMethod.PATCH,
            path=f'/api/expenses/update/{id}',
            json={
                'data': data,
                'amount': amount,
                'name': name,
                'attachments': attachments,
                'expense_category_id': expense_category_id,
            }
        )

    def delete_expenses(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.DELETE,
            path=f'/api/expenses/delete/{id}',

        )