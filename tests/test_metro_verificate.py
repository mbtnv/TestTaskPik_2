import json

async def test_verificate(client):
    response = await client.post('/api/v1/metro/verificate', data=json.dumps(test_data))
    assert response.status == 200
    assert await response.json() == test_response

test_data = [
	"Каховская",
	"Баррикадная",
	"Шоссе Энтузиастов",
	"Шоссе Энтузиастов",
    "New Station"
]

test_response = {
    "unchanged": [
        "Каховская",
        "Баррикадная",
        "Шоссе Энтузиастов",
        "Шоссе Энтузиастов"
    ],
    "updated": ["New Station"],
    "deleted": [
        "Новокосино",
        "Новогиреево",
        "Перово",
        "Авиамоторная",
        "Площадь Ильича",
        "Марксистская",
        "Третьяковская",
        "Третьяковская",
        "Ховрино",
        "Беломорская",
        "Речной вокзал",
        "Водный стадион",
        "Войковская",
        "Сокол",
        "Аэропорт",
        "Динамо",
        "Белорусская",
        "Белорусская",
        "Белорусская",
        "Маяковская",
        "Тверская",
        "Театральная",
        "Новокузнецкая",
        "Павелецкая",
        "Павелецкая",
        "Автозаводская",
        "Автозаводская",
        "Технопарк",
        "Коломенская",
        "Каширская",
        "Каширская",
        "Кантемировская",
        "Царицыно",
        "Царицыно",
        "Орехово",
        "Домодедовская",
        "Красногвардейская",
        "Алма-Атинская",
        "Медведково",
        "Бабушкинская",
        "Свиблово",
        "Ботанический сад",
        "Ботанический сад",
        "ВДНХ",
        "Алексеевская",
        "Рижская",
        "Рижская",
        "Проспект Мира",
        "Проспект Мира",
        "Сухаревская",
        "Тургеневская",
        "Китай-город",
        "Китай-город",
        "Октябрьская",
        "Октябрьская",
        "Шаболовская",
        "Ленинский проспект",
        "Академическая",
        "Профсоюзная",
        "Новые Черемушки",
        "Калужская",
        "Беляево",
        "Коньково",
        "Теплый Стан",
        "Ясенево",
        "Новоясеневская",
        "Бульвар Рокоссовского",
        "Бульвар Рокоссовского",
        "Черкизовская",
        "Преображенская площадь",
        "Сокольники",
        "Красносельская",
        "Комсомольская",
        "Комсомольская",
        "Красные ворота",
        "Чистые пруды",
        "Лубянка",
        "Охотный ряд",
        "Библиотека им.Ленина",
        "Кропоткинская",
        "Парк культуры",
        "Парк культуры",
        "Фрунзенская",
        "Спортивная",
        "Воробьевы горы",
        "Университет",
        "Проспект Вернадского",
        "Юго-Западная",
        "Тропарево",
        "Румянцево",
        "Саларьево",
        "Филатов луг",
        "Прокшино ",
        "Ольховая ",
        "Коммунарка",
        "Щелковская",
        "Первомайская",
        "Измайловская",
        "Партизанская",
        "Семеновская",
        "Электрозаводская",
        "Бауманская",
        "Площадь Революции",
        "Курская",
        "Курская",
        "Курская",
        "Арбатская",
        "Арбатская",
        "Смоленская",
        "Смоленская",
        "Киевская",
        "Киевская",
        "Киевская",
        "Парк Победы",
        "Парк Победы",
        "Славянский бульвар",
        "Кунцевская",
        "Кунцевская",
        "Кунцевская",
        "Молодежная",
        "Крылатское",
        "Строгино",
        "Мякинино",
        "Волоколамская",
        "Волоколамская",
        "Митино",
        "Пятницкое шоссе",
        "Пионерская",
        "Филевский парк",
        "Багратионовская",
        "Фили",
        "Фили",
        "Кутузовская",
        "Кутузовская",
        "Студенческая",
        "Александровский сад",
        "Выставочная",
        "Международная",
        "Алтуфьево",
        "Бибирево",
        "Отрадное",
        "Владыкино",
        "Владыкино",
        "Петровско-Разумовская",
        "Петровско-Разумовская",
        "Тимирязевская",
        "Тимирязевская",
        "Тимирязевская",
        "Дмитровская",
        "Дмитровская",
        "Савеловская",
        "Менделеевская",
        "Цветной бульвар",
        "Чеховская",
        "Боровицкая",
        "Полянка",
        "Серпуховская",
        "Тульская",
        "Нагатинская",
        "Нагорная",
        "Нахимовский проспект",
        "Севастопольская",
        "Чертановская",
        "Южная",
        "Пражская",
        "Улица Академика Янгеля",
        "Аннино",
        "Бульвар Дмитрия Донского",
        "Планерная",
        "Сходненская",
        "Тушинская",
        "Тушинская",
        "Спартак",
        "Щукинская",
        "Октябрьское поле",
        "Полежаевская",
        "Беговая",
        "Беговая",
        "Улица 1905 года",
        "Пушкинская",
        "Кузнецкий мост",
        "Таганская",
        "Таганская",
        "Пролетарская",
        "Волгоградский проспект",
        "Текстильщики",
        "Текстильщики",
        "Кузьминки",
        "Рязанский проспект",
        "Выхино",
        "Лермонтовский проспект",
        "Жулебино",
        "Котельники",
        "Новослободская",
        "Добрынинская",
        "Краснопресненская",
        "Селигерская",
        "Верхние Лихоборы",
        "Окружная",
        "Окружная",
        "Окружная",
        "Фонвизинская",
        "Бутырская ",
        "Марьина Роща",
        "Достоевская",
        "Трубная",
        "Сретенский бульвар",
        "Чкаловская",
        "Римская",
        "Крестьянская застава",
        "Дубровка",
        "Дубровка",
        "Кожуховская",
        "Печатники",
        "Волжская",
        "Люблино",
        "Братиславская",
        "Марьино",
        "Борисово",
        "Шипиловская",
        "Зябликово",
        "Варшавская",
        "Бунинская аллея",
        "Улица Горчакова",
        "Бульвар Адмирала Ушакова",
        "Улица Скобелевская",
        "Улица Старокачаловская",
        "Лесопарковая",
        "Битцевский Парк",
        "Петровский парк",
        "Петровский парк",
        "ЦСКА",
        "ЦСКА",
        "Хорошевская",
        "Хорошевская",
        "Шелепиха",
        "Шелепиха",
        "Шелепиха",
        "Деловой центр",
        "Деловой центр",
        "Деловой центр",
        "Минская",
        "Ломоносовский проспект",
        "Раменки",
        "Мичуринский проспект",
        "Озёрная",
        "Говорово ",
        "Солнцево",
        "Боровское шоссе",
        "Новопеределкино",
        "Рассказовка",
        "Савёловская",
        "Савёловская",
        "Савёловская",
        "Ростокино",
        "Белокаменная",
        "Локомотив",
        "Измайлово",
        "Соколиная Гора",
        "Андроновка",
        "Нижегородская",
        "Новохохловская",
        "Новохохловская",
        "Угрешская",
        "ЗИЛ",
        "Верхние Котлы",
        "Крымская",
        "Площадь Гагарина",
        "Лужники",
        "Хорошево",
        "Зорге",
        "Панфиловская",
        "Стрешнево",
        "Стрешнево",
        "Балтийская",
        "Коптево",
        "Лихоборы",
        "Улица Милашенкова",
        "Телецентр",
        "Улица Академика Королёва",
        "Выставочный центр",
        "Улица Сергея Эйзенштейна",
        "Косино",
        "Улица Дмитриевского ",
        "Лухмановская",
        "Некрасовка",
        "Лобня",
        "Шереметьевская",
        "Хлебниково",
        "Водники",
        "Долгопрудная",
        "Новодачная",
        "Марк",
        "Лианозово",
        "Бескудниково",
        "Дегунино",
        "Тестовская",
        "Рабочий Посёлок",
        "Сетунь",
        "Немчиновка",
        "Сколково",
        "Баковка",
        "Одинцово",
        "Нахабино",
        "Аникеевка",
        "Опалиха",
        "Красногорская",
        "Павшино",
        "Пенягино",
        "Покровское-Стрешнево",
        "Красный Балтиец",
        "Гражданская",
        "Каланчёвская",
        "Москва Товарная",
        "Калитники",
        "Кубанская",
        "Депо",
        "Перерва",
        "Москворечье",
        "Покровское",
        "Красный строитель",
        "Битца",
        "Бутово",
        "Щербинка",
        "Остафьево",
        "Силикатная",
        "Подольск",
        "Трикотажная"
    ]
}
