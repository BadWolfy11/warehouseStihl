from .API import API, RequestMethod

class Goods(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def all_goods(self, page: int, itemsPerPage: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/goods/get_paginated',
            params={
                'page': page,
                'itemsPerPage': itemsPerPage
            }
        )