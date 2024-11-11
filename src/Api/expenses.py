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