from locust import tag
from tasks.base import BaseUser


@tag('manWomenPage/manPage')
def load_man_page(user):
    user.client.get("/butik/liste/2/erkek?srsltid=AfmBOoo1gqoeAdBWC9DReRy8yd_bLp96Xeo1iPTZcDPnfKLGHgo99l8H")

@tag('manWomenPage/womenPage')
def load_women_page(user):
    user.client.get("/butik/liste/1/kadin")


class ManOrWomenPageUser(BaseUser):
    tasks = [load_man_page,
             load_women_page]
