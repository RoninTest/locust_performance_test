from tasks.homepage import HomePageUser
from tasks.loginpage import LoginPageUser
from tasks.manwomenpage import ManOrWomenPageUser
from tasks.productpage import ProductPageUser
from locust import between


class MyUser:
    wait_time = between(1, 40)
    tasks = [HomePageUser,
             ProductPageUser,
             ManOrWomenPageUser,
             LoginPageUser]
