from locust import tag
from tasks.base import BaseUser


@tag('homepage')
def load_homepage(user):
    user.client.get("/")


class HomePageUser(BaseUser):
    tasks = [load_homepage]
