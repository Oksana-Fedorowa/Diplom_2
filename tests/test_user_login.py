
import requests
from data import Data, UsersData, RespTextsData
import allure
from helpers import create_random_email, create_random_password

class TestUserLogin:
    @allure.title('Логин под существующим пользователем')
    @allure.description('Проверка успешного логина под существующим пользователем с валидными данными.')
    def test_login_with_existing_user(self):
        existing_user_data = {
            'email': UsersData.email,
            'password': UsersData.password
        }
        response = requests.post(Data.USER_AUTH, json=existing_user_data)
        response_body = response.json()
        assert (
                response.status_code == 200 and
                RespTextsData.TEXT_200_SUCCESS in response.text and
                'accessToken' in response_body and
                'refreshToken' in response_body
        )

    @allure.title('Логин с неверным логином и паролем')
    @allure.description(
        'Проверка логина с неверным email и паролем. Тест проверяет, что возвращается ошибка 401 с соответствующим сообщением.')
    def test_login_with_incorrect_email(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password()
        }
        response = requests.post(Data.USER_AUTH, json=payload)
        assert response.status_code == 401 and response.text == RespTextsData.TEXT_401_INCORRECT


