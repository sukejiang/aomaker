from requests import request

from aomaker.fixture import BaseLogin


class Login(BaseLogin):

    def login(self) -> dict:
        resp_login = {}
        return resp_login

    def make_headers(self, resp_login:dict) -> dict:
        headers = {
            'Cookie': f'csrftoken=aomakerniubility'}
        return headers
    