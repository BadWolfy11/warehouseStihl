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
