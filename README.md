# goit_python_core_hw_08

Source data:
```
[
    {'name': 'Зиновій Жук', 'birthday': datetime.date(2000, 7, 14)},
    {'name': 'Віра Проценко', 'birthday': datetime.date(1985, 7, 11)},
    {'name': 'пані Амалія Безбородько', 'birthday': datetime.date(1965, 7, 11)},
    {'name': 'Соломія Бандура', 'birthday': datetime.date(2000, 7, 3)},
    {'name': 'Зиновій Андрусенко', 'birthday': datetime.date(1972, 6, 29)},
    {'name': 'Гордій Девдюк', 'birthday': datetime.date(2002, 6, 25)},
    {'name': 'Георгій Шведченко', 'birthday': datetime.date(1974, 7, 17)},
    {'name': 'Сніжана Нестайко', 'birthday': datetime.date(1975, 6, 29)},
    {'name': 'Василь Терещенко', 'birthday': datetime.date(1994, 7, 11)},
    {'name': 'Аліна Їжак', 'birthday': datetime.date(1973, 7, 14)},
    {'name': 'Лілія Шамрай', 'birthday': datetime.date(1980, 7, 8)},
    {'name': 'Августин Терещенко', 'birthday': datetime.date(2004, 7, 8)},
    {'name': 'Соломія Засуха', 'birthday': datetime.date(1983, 6, 24)},
    {'name': 'Володимир Дейсун', 'birthday': datetime.date(1979, 7, 22)},
    {'name': 'Лукʼян Ґерус', 'birthday': datetime.date(1986, 7, 5)},
    {'name': 'пані Альбіна Засенко', 'birthday': datetime.date(1994, 7, 20)},
    {'name': 'Анжела Гаврилюк', 'birthday': datetime.date(1964, 6, 29)},
    {'name': 'Лесь Вовк', 'birthday': datetime.date(1996, 7, 20)},
    {'name': 'Камілла Алексюк', 'birthday': datetime.date(1979, 7, 8)},
    {'name': 'Еріка Лисенко', 'birthday': datetime.date(1992, 7, 16)},
    {'name': 'Пилип Чміль', 'birthday': datetime.date(2001, 7, 1)},
    {'name': 'Миколай Вовк', 'birthday': datetime.date(1981, 6, 24)},
    {'name': 'Ярослав Дзюба', 'birthday': datetime.date(2003, 7, 4)},
    {'name': 'Одарка Верховинець', 'birthday': datetime.date(1972, 7, 12)},
    {'name': 'Гаврило Деревʼянко', 'birthday': datetime.date(1996, 7, 15)},
    {'name': 'Данна Ткаченко', 'birthday': datetime.date(2001, 7, 18)},
    {'name': 'пані Клавдія Гресь', 'birthday': datetime.date(1994, 7, 18)},
    {'name': 'пан Соломон Гук', 'birthday': datetime.date(1980, 7, 6)},
    {'name': 'Мартин Матвієнко', 'birthday': datetime.date(1967, 7, 8)},
    {'name': 'Симон Безбородьки', 'birthday': datetime.date(1997, 6, 25)},
    {'name': 'Миколай Юрчук', 'birthday': datetime.date(1977, 6, 29)},
    {'name': 'Аніта Дробаха', 'birthday': datetime.date(1974, 6, 30)},
    {'name': 'Теодор Корсун', 'birthday': datetime.date(1980, 7, 11)},
    {'name': 'Соломон Оберемко', 'birthday': datetime.date(1964, 7, 1)},
    {'name': 'Руслан Колісниченко', 'birthday': datetime.date(1959, 6, 27)},
    {'name': 'Ярослава Тихий', 'birthday': datetime.date(1974, 7, 13)},
    {'name': 'Ірина Перепелиця', 'birthday': datetime.date(1963, 7, 8)},
    {'name': 'Іван Дубина', 'birthday': datetime.date(1976, 6, 25)},
    {'name': 'Захар Москаль', 'birthday': datetime.date(1991, 7, 11)},
    {'name': 'Маруся Шевченко', 'birthday': datetime.date(1967, 7, 7)},
    {'name': 'Леонід Скорик', 'birthday': datetime.date(1965, 6, 28)},
    {'name': 'пані Варвара Сіробаба', 'birthday': datetime.date(2000, 7, 18)},
    {'name': 'Михайлина Гаврилець', 'birthday': datetime.date(1981, 7, 17)},
    {'name': 'Богдан Запорожець', 'birthday': datetime.date(1962, 7, 8)},
    {'name': 'Одарка Петрик', 'birthday': datetime.date(1995, 7, 19)},
    {'name': 'Варвара Єрошенко', 'birthday': datetime.date(1984, 6, 27)},
    {'name': 'Віолетта Девдюк', 'birthday': datetime.date(1975, 6, 30)},
    {'name': 'Едуард Влох', 'birthday': datetime.date(1985, 7, 5)},
    {'name': 'пан Павло Вдовиченко', 'birthday': datetime.date(2001, 7, 22)},
    {'name': 'Феофан Гаврилишин', 'birthday': datetime.date(1982, 7, 21)}
]
```
Result:
```
понеділок, 26.06.2023 : ['Гордій Девдюк (2002-06-25), 21', 'Соломія Засуха (1983-06-24), 40', 'Миколай Вовк (1981-06-24), 42', 'Симон 
Безбородьки (1997-06-25), 26', 'Іван Дубина (1976-06-25), 47']
вівторок, 27.06.2023 : ['Руслан Колісниченко, 64', 'Варвара Єрошенко, 39']
середа, 28.06.2023 : ['Леонід Скорик, 58']
четвер, 29.06.2023 : ['Зиновій Андрусенко, 51', 'Сніжана Нестайко, 48', 'Анжела Гаврилюк, 59', 'Миколай Юрчук, 46']
п'ятниця, 30.06.2023 : ['Аніта Дробаха, 49', 'Віолетта Девдюк, 48']
```

