from .API import API, RequestMethod

class Categories(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def all_categories(self, offset: int, limit: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/categories/get_multi',
            params={
                'offset': offset,
                'limit': limit
            }
        )

    def new_categories(self, name: str) -> dict:
        return self.request(
            method=RequestMethod.POST,
            path='/api/categories/create',
            json={
                'name': name,
            }
        )

    def find_categories(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path=f'/api/categories/get/{id}',
        )

    def update_categories(self, id: int, data: str | None = None, name: str | None = None) -> dict:
        print(data)
        return self.request(
            method=RequestMethod.PATCH,
            path=f'/api/categories/update/{id}',
            json={
                'name': name
            }
        )

    def delete_categories(self, id: int) -> dict:
        return self.request(
            method=RequestMethod.DELETE,
            path=f'/api/categories/delete/{id}',

        )
