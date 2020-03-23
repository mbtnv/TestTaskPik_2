## Тестовое задание ПИК

### Запуск приложения
Перед запуском необходимо установить требуемые зависимости
```
pip install -r requirements.txt
```
```
python metro_verificate/main.py
```
Приложение будет запущено локально по адресу: http://localhost:8080

### Работа приложения
Приложение принимает POST запрос на endpoint **/api/v1/metro/verificate**, со списком станций в формате JSON.
```json
[
    "Каховская",
    "Баррикадная",
    "Шоссе Энтузиастов",
    "Новая Станция"
]
```
Сравнивает входящий список станций, со списком станций полученным из https://api.hh.ru/metro/1, и в результате возвращает следующий ответ, где **unchanged** - станции, которые присутствуют в обоих списках, **updated** - станции, которые отсутствуют в списке, полученном из внешнего API, **deleted** - станции, которые отсутствуют во входящем списке.
```json
{
    "unchanged": [
        "Каховская",
        "Баррикадная",
        "Шоссе Энтузиастов"
    ],
    "updated": [
        "Новая Станция"
    ],
    "deleted": [
        "Новокосино",
        "Новогиреево",
        "Перово",
        "Авиамоторная",
        "Площадь Ильича",
        ...
    ]
}

```
