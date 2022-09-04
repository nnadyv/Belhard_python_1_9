"""
Написать функцию check_phone, которая будет принимать строку и проверять,
что она соответствует шаблону:
1. код страны +375
2. код оператора 29, 33, 44, 25 в скобках
3. три цифры
4. тире
5. две цифры
6. тире
7 две цифры

Например: +375(29)365-12-12
"""
import re


def check_phone(phone):
    pattern = re.compile(r"^(\+375)(\(29\)|\(25\)|\(44\)|\(33\))(\d{3})(-)(\d{2})(-)(\d{2})$")
    if not pattern.match(phone):
        return False
    else:
        return True