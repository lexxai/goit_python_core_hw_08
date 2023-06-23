# goit_python_core_hw_08

Source data:

```
[
    {'name': 'Марина Запорожець', 'birthday': datetime.date(1992, 7, 5)},
    {'name': 'Віталій Сімашкевич', 'birthday': datetime.date(1985, 7, 5)},
    {'name': 'Надія Лавренко', 'birthday': datetime.date(1983, 7, 18)},
    {'name': 'Оксана Вдовенко', 'birthday': datetime.date(1974, 7, 19)},
    {'name': 'Амалія Цимбал', 'birthday': datetime.date(1959, 6, 27)},
    {'name': 'Ада Чалий', 'birthday': datetime.date(1997, 7, 15)},
    {'name': 'Назар Пʼятаченко', 'birthday': datetime.date(1977, 7, 14)},
    {'name': 'Орхип Атрощенко', 'birthday': datetime.date(1999, 7, 15)},
    {'name': 'Галина Вернидуб', 'birthday': datetime.date(1980, 7, 3)},
    {'name': 'Дарина Малик', 'birthday': datetime.date(1968, 7, 16)},
    {'name': 'Ірена Христенко', 'birthday': datetime.date(1971, 6, 25)},
    {'name': 'Юхим Конопленко', 'birthday': datetime.date(1992, 7, 16)},
    {'name': 'пані Христина Баран', 'birthday': datetime.date(1996, 7, 15)},
    {'name': 'Оксенія Дробʼязко', 'birthday': datetime.date(1992, 6, 24)},
    {'name': 'Камілла Микитюк', 'birthday': datetime.date(1986, 7, 13)},
    {'name': 'Тетяна Гузенко', 'birthday': datetime.date(1986, 7, 16)},
    {'name': 'Валентина Романець', 'birthday': datetime.date(1980, 6, 24)},
    {'name': 'Віра Жадан', 'birthday': datetime.date(1992, 6, 24)},
    {'name': 'Аврелій Іваничук', 'birthday': datetime.date(1992, 7, 17)},
    {'name': 'Роман Теличенко', 'birthday': datetime.date(1978, 7, 10)},
    {'name': 'Ада Заїка', 'birthday': datetime.date(1982, 7, 17)},
    {'name': 'Віталій Вівчаренко', 'birthday': datetime.date(1973, 7, 12)},
    {'name': 'Людмила Кармалюк', 'birthday': datetime.date(1993, 6, 29)},
    {'name': 'Арсен Дацюк', 'birthday': datetime.date(1989, 6, 30)},
    {'name': 'Орест Піддубний', 'birthday': datetime.date(1958, 7, 19)},
    {'name': 'Тереза Конопля', 'birthday': datetime.date(1974, 6, 30)},
    {'name': 'Роксолана Рева', 'birthday': datetime.date(1980, 7, 19)},
    {'name': 'Геннадій Тарасенко', 'birthday': datetime.date(1998, 7, 14)},
    {'name': 'пані Камілла Лазаренко', 'birthday': datetime.date(1997, 7, 3)},
    {'name': 'пані Лілія Килимник', 'birthday': datetime.date(1994, 7, 11)},
    {'name': 'Вʼячеслав Шиян', 'birthday': datetime.date(1986, 6, 30)},
    {'name': 'Юстина Рябченко', 'birthday': datetime.date(1965, 6, 24)},
    {'name': 'Світлана Якименко', 'birthday': datetime.date(1996, 7, 19)},
    {'name': 'Варфоломій Баклан', 'birthday': datetime.date(1991, 7, 19)},
    {'name': 'Єва Абраменко', 'birthday': datetime.date(1978, 7, 7)},
    {'name': 'Олесь Левченко', 'birthday': datetime.date(2001, 7, 9)},
    {'name': 'Гліб Тимчук', 'birthday': datetime.date(1985, 6, 26)},
    {'name': 'Варфоломій Іваненко', 'birthday': datetime.date(1973, 7, 20)},
    {'name': 'Марʼяна Медведенко', 'birthday': datetime.date(1989, 7, 15)},
    {'name': 'Федір Канівець', 'birthday': datetime.date(1967, 7, 12)},
    {'name': 'Назар Титаренко', 'birthday': datetime.date(1961, 6, 27)},
    {'name': 'пан Богодар Опанасенко', 'birthday': datetime.date(1977, 7, 20)},
    {'name': 'Петро Комар', 'birthday': datetime.date(1961, 7, 6)},
    {'name': 'Іван Скорик', 'birthday': datetime.date(1977, 7, 6)},
    {'name': 'Валерій Чалий', 'birthday': datetime.date(1963, 6, 28)},
    {'name': 'Михайлина Романенко', 'birthday': datetime.date(1961, 7, 16)},
    {'name': 'Богуслава Воблий', 'birthday': datetime.date(1995, 7, 12)},
    {'name': 'Тимофій Щорс', 'birthday': datetime.date(1975, 7, 9)},
    {'name': 'Софія Перебийніс', 'birthday': datetime.date(1967, 7, 3)},
    {'name': 'Світлана Корж', 'birthday': datetime.date(1958, 6, 28)}
]
```

Result:

```
понеділок, 26.06.2023 : ['Ірена Христенко (25.06.1971), 52', 'Оксенія Дробʼязко (24.06.1992), 31', 'Валентина Романець (24.06.1980),
43', 'Віра Жадан (24.06.1992), 31', 'Юстина Рябченко (24.06.1965), 58', 'Гліб Тимчук, 38']
вівторок, 27.06.2023 : ['Амалія Цимбал, 64', 'Назар Титаренко, 62']
середа, 28.06.2023 : ['Валерій Чалий, 60', 'Світлана Корж, 65']
четвер, 29.06.2023 : ['Людмила Кармалюк, 30']
п'ятниця, 30.06.2023 : ['Арсен Дацюк, 34', 'Тереза Конопля, 49', 'Вʼячеслав Шиян, 37']s
```
