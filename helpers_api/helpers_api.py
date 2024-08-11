from faker import Faker
from .conftest import api_client
class Endpoints:
    BASE = 'https://stellarburgers.nomoreparties.site/'
    AUTHORIZATION = 'api/auth/login'
    LOGOUT = 'api/auth/logout'
    TOKEN = 'api/auth/token'
    USER = 'api/auth/user'
    ORDERS = 'api/orders'
    ALL_ORDERS = 'api/orders/all'
    PASSWORD_RESET = 'api/password-reset'
    REGISTER = 'api/auth/register'
    ORDER_HISTORY = 'api/order-history'

class HttpMethods:
    get = 'GET'
    post = 'POST'
    patch = 'PATCH'
    delete = 'DELETE'


class HelpersApi:

    @staticmethod
    def generate_user_data():
        fake = Faker()
        random_login = fake.user_name()
        random_password = fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        random_email = fake.email()
        data = {
            'email': random_email,
            'password': random_password,
            'name': random_login
        }
        return data


    @staticmethod
    def create_user(api_client, data):
        user = api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        return user

    @staticmethod
    def create_user_without_data(api_client):
        data = HelpersApi.generate_user_data()
        api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        return data

    @staticmethod
    def authorize(api_client, user_data=False):
        if not user_data:
            user_data = HelpersApi.generate_user_data()
        HelpersApi.create_user(api_client, user_data)
        response = api_client.send_request(HttpMethods.post, Endpoints.AUTHORIZATION, user_data)
        return response.json()['accessToken']

    @staticmethod
    def create_user_and_order(api_client):
        user_data = HelpersApi.generate_user_data()
        HelpersApi.create_user(api_client, user_data)
        token = HelpersApi.authorize(api_client)
        order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa75"]}
        order = api_client.send_request(HttpMethods.post, Endpoints.ORDERS, order_data, headers={"Authorization": token})
        order_id = order.json()['order']['number']
        order_ingredients = order.json()['order']['ingredients'][0]['name']
        return order_id, order_ingredients
