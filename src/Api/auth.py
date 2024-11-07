from .API import API, RequestMethod

class Auth(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def login(self, login: str, password: str) -> dict:
        return self.request(
            method=RequestMethod.POST,
            path='/api/auth/login',
            json={
                'login': login,
                'password': password
            }
        )

    async def registration(self, login: str, password: str, password_confirm: str):
        # ....
        pass
