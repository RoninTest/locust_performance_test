from locust import tag
from tasks.base import BaseUser, config

product_page_endpoints = config['endpoints']['productPage']


@tag('productPage/Iphone')
def load_product_page_iphone(user):
    user.client.get(product_page_endpoints["iphone"])


@tag('productPage/Bag')
def load_product_page_bag(user):
    user.client.get(product_page_endpoints["bag"])


class ProductPageUser(BaseUser):
    tasks = [load_product_page_iphone,
             load_product_page_bag]
