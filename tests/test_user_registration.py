
import allure
from conftest import *

class TestRegistration:

    @allure.title('Создание уникального пользователя')
    @allure.description('Создается уникальный пользователь с данным  сгенерированными Faker, удаляется из базы '
                        'после теста. В ответе проверяются код и тело, включая '
                        ' проверку accessToken и refreshToken')
    def test_create_unique_user(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Data.USER_REGISTER, json=payload)
        response_body = response.json()
        assert (response.status_code == 200 and RespTextsData.TEXT_200_SUCCESS in response.text and
                RespTextsData.TEXT_200_TOKEN in response.text and response_body['user']['email'] == payload['email']
                and response_body['user']['name'] == payload['name'])
        access_token = response_body['accessToken']
        requests.delete(Data.USER_DELETE, headers={'Authorization': f'Bearer {access_token}'})

    @pytest.mark.usefixtures("create_new_user_and_delete")
    @allure.title('Создание пользователя с уже зарегистрированным email')
    @allure.description('Проверка создания пользователя с уже существующим email. '
                        'Тест создает пользователя с email, который уже зарегистрирован в системе, '
                        'и проверяет, что возвращается ошибка 403 с соответствующим сообщением.')
    def test_create_user_with_existing_email(self, create_new_user_and_delete):
        existing_user_data = {'email': UsersData.email, 'password': 'new_password123', 'name': 'NewName'}
        response = requests.post(Data.USER_REGISTER, json=existing_user_data)
        assert response.status_code == 403 and response.text == RespTextsData.TEXT_403_EXISTING


    @pytest.mark.parametrize("invalid_user_data", UsersData.credentials_with_empty_field)
    @allure.title('Создание пользователя с незаполненным обязательным полем')
    @allure.description('Проверка создания пользователя с отсутствующим обязательным полем. '
                        'Тест пытается создать пользователя с пропущенным email, именем или паролем и '
                        'проверяет, что возвращается ошибка 403 с соответствующим сообщением.')
    def test_create_user_with_missing_required_field(self, invalid_user_data):
        response = requests.post(Data.USER_REGISTER, json=invalid_user_data)
        assert (
                response.status_code == 403 and
                response.text == RespTextsData.TEXT_403_MISSING
        )
