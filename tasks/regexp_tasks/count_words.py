"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words(words):
    pattern = re.compile(r"\w+(-\w+)*")
    count = 0
    words1 = words.split()
    for i in words1:
        if pattern.match(i):
            count += 1
    return count
