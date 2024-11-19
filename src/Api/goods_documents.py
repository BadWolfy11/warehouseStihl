from .API import API, RequestMethod

class GoodsDocuments(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def all_expenses(self, limit: int, offset: int) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path='/api/goods_documents/dump',
            params={
                'limit': limit,
                'offset': offset
            }
        )