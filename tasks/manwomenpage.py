from locust import tag
from tasks.base import BaseUser, config

menWomenPage_endpoints = config['endpoints']['menOrWomenPage']


@tag('menWomenPage/manPage')
def load_men_page(user):
    user.client.get(menWomenPage_endpoints["men"])


@tag('menWomenPage/womenPage')
def load_women_page(user):
    user.client.get(menWomenPage_endpoints["women"])


class ManOrWomenPageUser(BaseUser):
    tasks = [load_men_page,
             load_women_page]
