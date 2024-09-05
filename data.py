from helpers import *
class Data:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    USER_REGISTER = f'{BASE_URL}/api/auth/register' #Создание пользователя
    USER_AUTH = f'{BASE_URL}/api/auth/login' #эндпоинт для авторизации.
    USER_UPDATE = f'{BASE_URL}/api/auth/user' #эндпоинт получения данных о пользователе.
    USER_DELETE = f'{BASE_URL}/api/auth/user' #Удаление пользователя
    ORDER_CREATE = f'{BASE_URL}/api/orders' #Получить заказы конкретного пользователя
    GET_USER_ORDERS = f'{BASE_URL}/api/orders'
    HEADERS = {'Content-Type': 'application/json'}

class UsersData:
    email = 'oksana_fedorowa_11_111@ya.ru'
    password = 'pasword123'
    username = 'Oksana'

    credentials_with_empty_field = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''
         }
    ]


class IngredientData:
    BURGER_INGREDIENT_1 = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
                         '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    BURGER_INGREDIENT_2 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                           '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']


    INVALID_HASH_INGREDIENT = '61c0c5a71d1f7128389494f' #придуманный несуществующие ингридиенты

class RespTextsData:

    TEXT_200_SUCCESS = '"success":true'
    TEXT_200_TOKEN ='accessToken'


    TEXT_400_ORDER = '{"success":false,"message":"Ingredient ids must be provided"}'

    TEXT_401_INCORRECT = '{"success":false,"message":"email or password are incorrect"}'
    TEXT_401_UNAUTHORISED = '{"success":false,"message":"You should be authorised"}'

    TEXT_403_EXISTING = '{"success":false,"message":"User already exists"}'
    TEXT_403_MISSING = '{"success":false,"message":"Email, password and name are required fields"}'

    TEXT_500 = "Internal Server Error"