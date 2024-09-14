from locust import tag
from tasks.base import BaseUser


@tag('productPage/Iphone')
def load_product_page_iphone(user):
    user.client.get("/sr?rb=1617")


@tag('productPage/Bag')
def load_product_page_bag(user):
    user.client.get("/sr/?q=canta&qt=çanta&st=çanta")


class ProductPageUser(BaseUser):
    tasks = [load_product_page_iphone,
             load_product_page_bag]
