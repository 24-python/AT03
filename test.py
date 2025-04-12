import pytest  # Импортируем pytest — фреймворк для тестирования
from main import get_cat_image

#from main import get_github_user
# from main import get_weather  # Импортируем функцию get_weather из модуля main
#
#
# # Первый тест: проверка успешного получения погоды
# def test_get_weather(mocker):
#     # Подменяем вызов requests.get внутри функции get_weather
#     mock_get = mocker.patch('main.requests.get')
#
#     # Устанавливаем статус ответа 200 (успех)
#     mock_get.return_value.status_code = 200
#
#     # Устанавливаем возвращаемые данные (то, что вернёт response.json())
#     mock_get.return_value.json.return_value = {
#         'description': [{'clear sky'}],  # Пример данных о погоде
#         'main': {'temp': 10}  # Температура
#     }
#
#     # Подготавливаем тестовые значения ключа API и города
#     api_key = '10ba5048f8830fa351ec0249131fa297'
#     city = 'Moscow'
#
#     # Вызываем функцию, которая теперь использует замоканный requests.get
#     weather_data = get_weather(api_key, city)
#
#     # Проверяем, что результат соответствует ожидаемому
#     assert weather_data == {
#         'description': [{'clear sky'}],
#         'main': {'temp': 10}
#     }
#
#
# # Второй тест: проверка обработки ошибки (например, 404 от сервера)
# def test_get_github_user_with_error(mocker):
#     # Также подменяем requests.get
#     mock_get = mocker.patch('main.requests.get')
#
#     # Устанавливаем ошибочный статус (например, 404 Not Found)
#     mock_get.return_value.status_code = 404
#
#     # Подготавливаем те же параметры
#     api_key = '10ba5048f8830fa351ec0249131fa297'
#     city = 'Moscow'
#
#     # Вызываем функцию — она должна вернуть None при 404
#     weather_data = get_weather(api_key, city)
#
#     # ❗ ВНИМАНИЕ: здесь тест написан с ошибкой — функция должна возвращать None,
#     # а тест почему-то ожидает структуру с погодой, что не соответствует логике
#     assert weather_data == None

def test_get_cat_image_success(mocker):
    # Ожидаемый URL от API
    expected_url = 'https://cdn.thecatapi.com/images/abc123.jpg'

    # Подменяем requests.get
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': expected_url}]

    # Вызываем тестируемую функцию
    result = get_cat_image()

    # Проверяем, что результат — это ожидаемый URL
    assert result == expected_url


def test_get_cat_image_failure(mocker):
    # Подменяем requests.get внутри модуля
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404  # Симулируем ошибку 404

    # Вызываем функцию
    result = get_cat_image()

    # Проверяем, что результат — None при ошибке
    assert result is None