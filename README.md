# tz_infotecs

Методы API

CityDetailView
Получение информации о городе по geonameid
URL: /city/<int:geonameid>/
Метод: GET
Параметры URL: geonameid - идентификатор города
Ответ: Информация о городе в формате JSON

CityListView
Получение списка городов
URL: /cities/
Метод: GET
Параметры запроса: page - номер страницы, per_page - количество городов на странице
Ответ: Список городов в формате JSON

CityComparisonView
Сравнение городов
URL: /compare-cities/
Метод: GET
Параметры запроса: city1 - название первого города, city2 - название второго города
Ответ: Результат сравнения городов в формате JSON

CityAutocompleteView
Автозаполнение названий городов
URL: /help_search/
Метод: GET
Параметры запроса: query - часть названия города
Ответ: Список совпадающих названий городов в формате JSON

УСТАНОВКА
1. Клонируйте репозиторий: https://github.com/Kapitan21oo/tz_infotecs.git
2. Перейдите в папку проекта: cd tz_infotecs
3. Войдите в корень проекта: cd main
4. Установите список зависимостей: pip install -r requirements.txt

ЗАПУСК
1. Создайте и выполните миграции: python manage.py makemigrations / python manage.py migrate
2. Загрузите данные о географических названиях: python manage.py load_geonames
3. Запустите сервер: python manage.py runserver
