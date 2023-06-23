# goit_python_core_hw_08

Source data:

```
[
    {'name': 'Марина Сиротенко', 'birthday': datetime.date(1980, 7, 19)},
    {'name': 'Оксана Євдокименко', 'birthday': datetime.date(1972, 7, 18)},
    {'name': 'Юстим Данько', 'birthday': datetime.date(1983, 7, 8)},
    {'name': 'Володимир Семенченко', 'birthday': datetime.date(1973, 7, 13)},
    {'name': 'пані Мілена Чміль', 'birthday': datetime.date(2003, 6, 25)},
    {'name': 'Аніта Полтавець', 'birthday': datetime.date(1999, 7, 17)},
    {'name': 'Валерій Черненко', 'birthday': datetime.date(1965, 7, 12)},
    {'name': 'Едита Акуленко', 'birthday': datetime.date(1983, 7, 1)},
    {'name': 'Людмила Твердохліб', 'birthday': datetime.date(1973, 7, 7)},
    {'name': 'Борис Захарченко', 'birthday': datetime.date(1988, 6, 27)},
    {'name': 'Орина Товстоліс', 'birthday': datetime.date(1976, 7, 10)},
    {'name': 'Оксана Єресько', 'birthday': datetime.date(1990, 7, 20)},
    {'name': 'Дарина Харченко', 'birthday': datetime.date(1981, 7, 8)},
    {'name': 'Алевтин Данченко', 'birthday': datetime.date(1964, 6, 26)},
    {'name': 'Охрім Байрак', 'birthday': datetime.date(1980, 6, 29)},
    {'name': 'Емілія Лукаш', 'birthday': datetime.date(2004, 6, 29)},
    {'name': 'Валентин Козаченко', 'birthday': datetime.date(1989, 6, 27)},
    {'name': 'Симон Шахрай', 'birthday': datetime.date(2003, 6, 30)},
    {'name': 'Марʼяна Архипенко', 'birthday': datetime.date(1982, 7, 16)},
    {'name': 'Христина Назаренко', 'birthday': datetime.date(1978, 6, 25)},
    {'name': 'Давид Саченко', 'birthday': datetime.date(1990, 7, 6)},
    {'name': 'Франц Бевзенко', 'birthday': datetime.date(1962, 7, 17)},
    {'name': 'Володимир Козаченко', 'birthday': datetime.date(1989, 6, 30)},
    {'name': 'Демʼян Ісаєнко', 'birthday': datetime.date(1964, 7, 9)},
    {'name': 'Роман Гречаник', 'birthday': datetime.date(1996, 7, 16)},
    {'name': 'Варвара Гупало', 'birthday': datetime.date(1964, 7, 11)},
    {'name': 'Віолетта Малик', 'birthday': datetime.date(2003, 6, 25)},
    {'name': 'Теодор Заруба', 'birthday': datetime.date(1993, 6, 30)},
    {'name': 'Костянтин Копитко', 'birthday': datetime.date(1985, 6, 25)},
    {'name': 'Розалія Засядько', 'birthday': datetime.date(1961, 7, 16)},
    {'name': 'Гордій Гайда', 'birthday': datetime.date(1968, 7, 4)},
    {'name': 'Пріска Демʼяненко', 'birthday': datetime.date(1996, 6, 29)},
    {'name': 'Мирон Заєць', 'birthday': datetime.date(1983, 7, 17)},
    {'name': 'Яків Луценко', 'birthday': datetime.date(1966, 7, 20)},
    {'name': 'Зиновій Жайворон', 'birthday': datetime.date(1983, 7, 21)},
    {'name': 'Надія Ґереґа', 'birthday': datetime.date(1999, 7, 13)},
    {'name': 'Оксана Цушко', 'birthday': datetime.date(1977, 7, 8)},
    {'name': 'Любов Дашкевич', 'birthday': datetime.date(1964, 7, 4)},
    {'name': 'Дарина Єрошенко', 'birthday': datetime.date(1977, 7, 22)},
    {'name': 'Оксенія Чабан', 'birthday': datetime.date(1989, 6, 26)},
    {'name': 'Василина Деркач', 'birthday': datetime.date(1994, 7, 2)},
    {'name': 'пан Борислав Данькевич', 'birthday': datetime.date(1968, 7, 9)},
    {'name': 'Гліб Фастенко', 'birthday': datetime.date(1959, 7, 3)},
    {'name': 'Максим Христич', 'birthday': datetime.date(1988, 7, 3)},
    {'name': 'Тереза Вернигора', 'birthday': datetime.date(1960, 7, 14)},
    {'name': 'Арсен Барабаш', 'birthday': datetime.date(2001, 7, 7)},
    {'name': 'Сергій Кириленко', 'birthday': datetime.date(1968, 7, 16)},
    {'name': 'пан Соломон Вернигора', 'birthday': datetime.date(1980, 7, 1)},
    {'name': 'Роксолана Алексеєнко', 'birthday': datetime.date(1980, 7, 6)},
    {'name': 'пані Анжела Матвієнко', 'birthday': datetime.date(1976, 6, 28)}
]
```

Result:

```
понеділок, 26.06.2023 : ['пані Мілена Чміль (25.06.2003), 20*', 'Алевтин Данченко, 59', 'Христина Назаренко (25.06.1978), 45*',
'Віолетта Малик (25.06.2003), 20*', 'Костянтин Копитко (25.06.1985), 38', 'Оксенія Чабан, 34']
вівторок, 27.06.2023 : ['Борис Захарченко, 35*', 'Валентин Козаченко, 34']
середа, 28.06.2023 : ['пані Анжела Матвієнко, 47']
четвер, 29.06.2023 : ['Охрім Байрак, 43', 'Емілія Лукаш, 18', 'Пріска Демʼяненко, 27']
п'ятниця, 30.06.2023 : ['Симон Шахрай, 19', 'Володимир Козаченко, 34', 'Теодор Заруба, 30*']
```
