from conftest import *
import requests
import allure

class TestGetOrders:
    @allure.title('Проверка успешного получения списка заказов авторизованного пользователя')
    def test_receive_orders_authorized_user(self, create_user_and_order_and_delete):
        headers = {'Authorization': create_user_and_order_and_delete[0]}
        response = requests.get(Data.GET_USER_ORDERS, headers=headers)
        response_body = response.json()
        assert (response.status_code == 200 and RespTextsData.TEXT_200_SUCCESS in response.text and 'orders' in
                response_body and 'total' in response_body)

    @allure.title('Проверка ответа при запросе на получение списка заказов неавторизованного пользователя')
    def test_receive_orders_unauthorized_user(self):
        response = requests.get(Data.GET_USER_ORDERS, headers=Data.HEADERS)
        assert response.status_code == 401 and  RespTextsData.TEXT_401_UNAUTHORISED