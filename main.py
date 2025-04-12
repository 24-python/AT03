import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов


# # Функция для получения информации о погоде (точнее, координат города через OpenWeatherMap Geo API)
# def get_weather(api_key, city):
#     # Формируем URL для API-запроса с указанием города, лимитом в 5 результатов и API-ключом
#     url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'
#
#     # Выполняем GET-запрос к указанному URL
#     response = requests.get(url)
#
#     # Если ответ от сервера успешный (код 200)
#     if response.status_code == 200:
#         # Преобразуем полученные данные из JSON-формата в Python-объект (список/словарь)
#         data = response.json()
#         # Возвращаем полученные данные
#         return data
#     else:
#         # Если произошла ошибка (например, неправильный ключ или город не найден), возвращаем None
#         return None


# def get_github_user(username):
#     url = f'https://api.github.com/users/{username}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
#

def get_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'  # URL запроса к API
    response = requests.get(url)                         # GET-запрос к API
    if response.status_code == 200:                      # Проверка, что всё прошло успешно
        return response.json()[0]['url']                 # Возврат ссылки на изображение
    else:
        return None                                      # В случае ошибки — вернуть None