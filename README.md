Scooter API autotests

Автоматизированный API-тест для сервиса аренды самокатов.

Тест реализует сценарий:
- создание заказа;
- получение заказа по трек-номеру;
- проверка корректного ответа сервера.

Технологии

- Python 3.10+
- pytest
- requests

Структура проекта

scooter-api-autotests/
├── tests/
│ └── test_order_track.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md

Описание автотеста

Автотест выполняет следующий сценарий:

1. Отправляет POST-запрос на создание заказа `/api/v1/orders`
2. Сохраняет трек-номер заказа из ответа
3. Отправляет GET-запрос на получение заказа по треку `/api/v1/orders/track`
4. Проверяет, что сервер возвращает код ответа `200`

Подготовка окружения

bash
pip install -r requirements.txt

Настройка

Base URL сервиса задаётся в файле config.py:

BASE_URL = "https://<your-stand>.serverhub.praktikum-services.ru"

Запуск тестов
pytest

Примечания

Тест проверяет работу API.

Логи находятся в /var/www/backend/logs/error.log.