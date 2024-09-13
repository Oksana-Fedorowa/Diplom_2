
import allure
from conftest import *

class TestOrderCreation:
    @allure.title('Создание заказа с авторизацией')
    @allure.description('Проверка успешного создания заказа при наличии валидного токена и корректных данных с указанными ингредиентами.')
    def test_create_order_with_authorization(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {
            "ingredients": IngredientData.BURGER_INGREDIENT_1
        }
        response = requests.post(Data.ORDER_CREATE, json=payload, headers=headers)
        response_body = response.json()
        assert (response.status_code == 200 and RespTextsData.TEXT_200_SUCCESS in response.text and 'order' in response_body
                and 'number' in response_body['order'])

    @allure.title('Создание заказа без авторизации')
    @allure.description ('Проверка успешного создания заказа с указанными ингредиентами .Токен аккаунта не передается')
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": IngredientData.BURGER_INGREDIENT_1
        }
        response = requests.post(Data.ORDER_CREATE, json=payload, headers=Data.HEADERS)
        assert response.status_code == 200 and RespTextsData.TEXT_200_SUCCESS in response.text

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Проверка ответа сервера при попытке создать заказ без указания ингредиентов.')
    def test_create_order_without_ingredients(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {
            "ingredients": []
        }
        response = requests.post(Data.ORDER_CREATE, json=payload, headers=headers)
        assert response.status_code == 400 and RespTextsData.TEXT_400_ORDER in response.text

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    @allure.description('Проверка ответа сервера при попытке создать заказ с неверным хешем ингредиентов.')
    def test_create_order_with_invalid_ingredient_hash(self, create_new_user_and_delete):
        payload = {
            "ingredients": [IngredientData.INVALID_HASH_INGREDIENT]
        }
        response = requests.post(Data.ORDER_CREATE, json=payload, headers=Data.HEADERS)
        assert response.status_code == 500 and RespTextsData.TEXT_500 in response.text
