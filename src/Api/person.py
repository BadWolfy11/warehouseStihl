from .API import API, RequestMethod

class Person(API):
    def __init__(self, token: str | None):
        super().__init__(token)

    def find_person(self, id: str) -> dict:
        return self.request(
            method=RequestMethod.GET,
            path=f'/api/person/get/{id}',

        )