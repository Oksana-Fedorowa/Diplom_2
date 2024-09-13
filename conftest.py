import pytest
import requests
from data import *

@pytest.fixture
def create_new_user_and_delete(): #Фикстура создает пользователя и удаляет его из базы после теста
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    } #создаем словарь содержащий данные для регистрации нового пользователя.
    response = requests.post(Data.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Data.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
def create_order_for_user(create_new_user_and_delete): #Фикстура создает заказ
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [IngredientData.BURGER_INGREDIENT_2]}
    response = requests.post(Data.ORDER_CREATE,  json=payload, headers=headers)

    yield access_token


