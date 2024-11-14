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

    def new_goods(self, barcode: str, name: str, description: str, category_id: int, attachments: str) -> dict:
        return self.request(
            method=RequestMethod.POST,
            path='/api/goods/create',
            json={
                'barcode': barcode,
                'name': name,
                'description': description,
                'category_id': category_id,
                'attachments': attachments
            }
        )

    def find_good(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path=f'/api/goods/get/{id}',
        )

    def update_good(self, id: int, barcode: str | None = None , name: str | None = None, description: str | None = None, category_id: int | None = None, attachments: str | None = None) -> dict:
        return self.request(
            method=RequestMethod.PATCH,
            path=f'/api/goods/update/{id}',
            json = {
                'barcode': barcode,
                'name': name,
                'description': description,
                'category_id': category_id,
                'attachments': attachments
            }
        )

    def delete_good(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.DELETE,
            path=f'/api/goods/delete/{id}',

        )