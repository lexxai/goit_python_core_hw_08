# goit_python_core_hw_08

Source data:

```
[
    {'name': 'Златослава Адамчук', 'birthday': datetime.date(1970, 7, 12)},
    {'name': 'Марʼяна Бабій', 'birthday': datetime.date(1998, 6, 25)},
    {'name': 'Едита Закусило', 'birthday': datetime.date(1963, 7, 11)},
    {'name': 'Олена Шахрай', 'birthday': datetime.date(2003, 7, 4)},
    {'name': 'Мирослав Андрієнко', 'birthday': datetime.date(1968, 7, 15)},
    {'name': 'Лариса Оніщук', 'birthday': datetime.date(1972, 7, 15)},
    {'name': 'Одарка Баранник', 'birthday': datetime.date(1960, 7, 15)},
    {'name': 'Одарка Ільченко', 'birthday': datetime.date(1974, 6, 29)},
    {'name': 'Оксенія Рак', 'birthday': datetime.date(1986, 7, 12)},
    {'name': 'Едуард Цимбал', 'birthday': datetime.date(1966, 6, 26)},
    {'name': 'Мілена Девдюк', 'birthday': datetime.date(1971, 7, 5)},
    {'name': 'Валерій Ващенко-Захарченко', 'birthday': datetime.date(1967, 7, 4)},
    {'name': 'Феофан Бандура', 'birthday': datetime.date(1993, 7, 21)},
    {'name': 'пан Олесь Бакуменко', 'birthday': datetime.date(1977, 7, 13)},
    {'name': 'Ада Василевич', 'birthday': datetime.date(1980, 7, 16)},
    {'name': 'Оксана Абраменко', 'birthday': datetime.date(2001, 6, 24)},
    {'name': 'Федір Дейнеко', 'birthday': datetime.date(1961, 6, 25)},
    {'name': 'Тереза Міщенко', 'birthday': datetime.date(1997, 7, 20)},
    {'name': 'Аарон Бабенко', 'birthday': datetime.date(1989, 7, 15)},
    {'name': 'Пантелеймон Журба', 'birthday': datetime.date(1977, 7, 9)},
    {'name': 'Роксолана Рябошапка', 'birthday': datetime.date(1965, 7, 19)},
    {'name': 'Гліб Хмара', 'birthday': datetime.date(1988, 6, 24)},
    {'name': 'Ярослава Притула', 'birthday': datetime.date(1971, 7, 11)},
    {'name': 'Марія Дубас', 'birthday': datetime.date(1977, 6, 24)},
    {'name': 'Ярослава Вахній', 'birthday': datetime.date(1993, 7, 18)},
    {'name': 'Владислав Гаєвський', 'birthday': datetime.date(1991, 7, 16)},
    {'name': 'Охрім Левченко', 'birthday': datetime.date(2001, 6, 30)},
    {'name': 'Варвара Петрик', 'birthday': datetime.date(1958, 7, 21)},
    {'name': 'Георгій Бевзенко', 'birthday': datetime.date(1966, 7, 6)},
    {'name': 'Нестор Дубас', 'birthday': datetime.date(1975, 7, 22)},
    {'name': 'Богуслав Салій', 'birthday': datetime.date(1981, 7, 10)},
    {'name': 'Віолетта Чабан', 'birthday': datetime.date(1996, 7, 19)},
    {'name': 'Валентин Приходько', 'birthday': datetime.date(1998, 7, 7)},
    {'name': 'пан Олег Валенко', 'birthday': datetime.date(1970, 7, 17)},
    {'name': 'Ярослава Лазаренко', 'birthday': datetime.date(1990, 6, 29)},
    {'name': 'Святослав Абрагамовський', 'birthday': datetime.date(1998, 7, 11)},
    {'name': 'Святослав Козак', 'birthday': datetime.date(1988, 6, 29)},
    {'name': 'Лукʼян Вівчаренко', 'birthday': datetime.date(1978, 7, 8)},
    {'name': 'Леон Теліженко', 'birthday': datetime.date(1963, 7, 16)},
    {'name': 'Остап Вертипорох', 'birthday': datetime.date(1977, 6, 28)},
    {'name': 'Герман  Абрамчук', 'birthday': datetime.date(1982, 7, 15)},
    {'name': 'Панас Бабак', 'birthday': datetime.date(1993, 6, 28)},
    {'name': 'Сергій Голобородько', 'birthday': datetime.date(1982, 7, 3)},
    {'name': 'Богуслав Черненко', 'birthday': datetime.date(1974, 7, 7)},
    {'name': 'Дарина Адаменко', 'birthday': datetime.date(1989, 7, 16)},
    {'name': 'Оксенія Хомик', 'birthday': datetime.date(1981, 7, 8)},
    {'name': 'Степан Шаблій', 'birthday': datetime.date(2000, 7, 16)},
    {'name': 'Ярослава Баранник', 'birthday': datetime.date(1999, 7, 20)},
    {'name': 'Дан Притула', 'birthday': datetime.date(1981, 7, 18)},
    {'name': 'Лесь Бакуменко', 'birthday': datetime.date(1999, 7, 9)}
]
```

Result:

```
понеділок, 26.06.2023 : ['Марʼяна Бабій (25.06.1998), 25', 'Едуард Цимбал, 57', 'Оксана Абраменко (24.06.2001), 22', 'Федір Дейнеко
(25.06.1961), 62', 'Гліб Хмара (24.06.1988), 35', 'Марія Дубас (24.06.1977), 46']
середа, 28.06.2023 : ['Остап Вертипорох, 46', 'Панас Бабак, 30*']
четвер, 29.06.2023 : ['Одарка Ільченко, 49', 'Ярослава Лазаренко, 33', 'Святослав Козак, 35']
п'ятниця, 30.06.2023 : ['Охрім Левченко, 21']
```
