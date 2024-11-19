from .API import API, RequestMethod

class ExpenseCategories(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def all_expense_categories(self, offset: int, limit: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/expense_categories/get_multi',
            params={
                'offset': offset,
                'limit': limit
            }

        )

    def all_exp_categories(self, page: int, itemsPerPage: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/expense_categories/get_paginated',
            params={
                'page': page,
                'itemsPerPage': itemsPerPage
            }
        )

    def new_exp_categories(self, name: str) -> dict:
        return self.request(
            method=RequestMethod.POST,
            path='/api/expense_categories/create',
            json={
                'name': name,
            }
        )

    def find_exp_categories(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path=f'/api/expense_categories/get/{id}',
        )

    def update_exp_categories(self, id: int, data: str | None = None, name: str | None = None) -> dict:
        print(data)
        return self.request(
            method=RequestMethod.PATCH,
            path=f'/api/expense_categories/update/{id}',
            json={
                'name': name
            }
        )

    def delete_exp_categories(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.DELETE,
            path=f'/api/expense_categories/delete/{id}',

        )

