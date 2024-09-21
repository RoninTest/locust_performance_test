from locust import tag

from tasks.base import BaseUser, config

login_page_endpoints = config['endpoints']['loginPage']


@tag('loginPage/loginMainPage')
def load_login_page(user):
    user.client.get(login_page_endpoints["loginMainPage"])


class LoginPageUser(BaseUser):
    tasks = [load_login_page]
