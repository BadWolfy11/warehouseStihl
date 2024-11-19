from .API import API, RequestMethod

class Role(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def all_roles(self, page: int, itemsPerPage: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/role/get_paginated',
            params={
                'page': page,
                'itemsPerPage': itemsPerPage
            }
        )

    def new_roles(self, name: str) -> dict:
        return self.request(
            method=RequestMethod.POST,
            path='/api/role/create',
            json={
                'name': name,
            }
        )

    def find_roles(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path=f'/api/role/get/{id}',
        )

    def update_roles(self, id: int, data: str | None = None, name: str | None = None) -> dict:
        print(data)
        return self.request(
            method=RequestMethod.PATCH,
            path=f'/api/role/update/{id}',
            json={
                'name': name
            }
        )

    def delete_roles(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.DELETE,
            path=f'/api/role/delete/{id}',

        )
