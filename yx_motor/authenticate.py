# AUTOGENERATED! DO NOT EDIT! File to edit: 04_authenticate.ipynb (unless otherwise specified).

__all__ = ["Authenticate"]

# Cell
import requests

from .api import API


class Authenticate:
    "Class for handling authenticate API actions"

    def __init__(self, api: API):
        self.api = api
        self.base_endpoint = "authenticate/"

    def authenticate(self, login_email: str, login_pwd: str) -> requests.Response:
        payload = {"email": login_email, "password": login_pwd}
        response = self.api.post(url=self.base_endpoint, json=payload)
        if response.status_code == 200:
            self.api.jar.update(response.cookies)
            self.api.is_authenticated = True
        return response

    def logout(self):
        logout_endpoint = f"{self.base_endpoint}logout"
        response = self.api.post(url=logout_endpoint)
        if response.status_code == 204:
            self.api.jar.update(response.cookies)
            self.api.is_authenticated = False
        return response
