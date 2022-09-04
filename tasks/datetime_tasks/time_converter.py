"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""
import datetime

import pytz


def convert_date(timestamp, current_zone, new_zone):
    current_zone = pytz.timezone(current_zone)
    new_zone = pytz.timezone(new_zone)
    timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    timestamp = current_zone.localize(timestamp)
    timestamp = timestamp.astimezone(new_zone)
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp
