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
