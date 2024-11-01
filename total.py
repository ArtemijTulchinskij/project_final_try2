import requests #библиотека ответов

URL_SERVER = "https://62b675f2-a048-43f1-9566-26da49ca8891.serverhub.praktikum-services.ru" #сервер
#ручки
CREATE_ORDER = "/api/v1/orders"
GET_ORDER_TRACK = "/api/v1/orders/track"

# Step 1: Создание заказа
def create_order():
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    response = requests.post(URL_SERVER + CREATE_ORDER, json=payload)
    assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
    track = response.json()["track"]
    print("Заказ создан. Номер трека:", track)
    return track

# Step 2: Получение заказа по треку
def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(URL_SERVER + GET_ORDER_TRACK, params=params)
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    print("Заказ успешно получен. Ответ:", response.json())
    return response.json()

# Main test
def test_create_and_get_order():
    track = create_order()
    order_data = get_order_by_track(track)
    assert order_data["order"]["track"] == track, "Номер трека не совпадает"
    print("Тест успешно пройден.")

# Запуск теста
if __name__ == "__main__":
    test_create_and_get_order()
