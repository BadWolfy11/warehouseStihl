from pydantic import BaseModel, Field
from enum import Enum
from typing import Any
import requests
import json


class RequestMethod(str, Enum):
    GET = 'get'
    POST = 'post'
    PATCH = 'patch'
    PUT = 'put'
    DELETE = 'delete'


class API:
    def __init__(self, token: str | None = None):
        self.base_url: str = 'http://127.0.0.1:8000'
        self.token: str | None = token

    def request(self, method: str, path: str, params={}, headers={}, data=None, json=None, tries=5, **kwargs):
        error = None

        for i in range(tries):
            try:
                headers.update({
                    'Authorization': f'Bearer {self.token}'
                })

                response = requests.request(
                    method=method,
                    url=f'{self.base_url}{path}',
                    headers=headers,
                    data=data,
                    json=json,
                    params=params
                )
                return {
                 'status': response.status_code,
                 'headers': response.headers,
                 'body': self.isJson(response.text),
                 }
            except Exception as err:
                error = err

        if error:
            raise error

    def isJson(self, data):
        try:
            return json.loads(data)
        except:
            return data