import allure
from conftest import *

class TestUserUpdate:
    updated_user_data = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }

    @allure.title('Изменение данных пользователя с авторизацией')
    @allure.description('Проверка успешного изменения данных пользователя при наличии валидного токена. '
                        'Изменяются поля: email  имя и пароль. Проверяется успешность операции и обновление данных.')
    def test_update_user_with_authorization(self, create_new_user_and_delete):
        response = requests.patch(Data.USER_UPDATE, headers={
            'Authorization': create_new_user_and_delete[1]["accessToken"]},
                                  json=TestUserUpdate.updated_user_data)
        response_body = response.json()
        assert (
                response.status_code == 200 and
                RespTextsData.TEXT_200_SUCCESS in response.text and
                response_body['user']['email'] == TestUserUpdate.updated_user_data['email'] and
                response_body['user']['name'] == TestUserUpdate.updated_user_data['name']
        )

    @allure.title('Попытка изменения данных пользователя без авторизации')
    @allure.description(
        'Проверка, что система возвращает ошибку при попытке изменить данные пользователя без авторизации. ')
    def test_update_user_without_authorization(self):
        response = requests.patch(Data.USER_UPDATE, headers=Data.HEADERS, json=TestUserUpdate.updated_user_data)
        assert response.status_code == 401 and RespTextsData.TEXT_401_UNAUTHORISED







