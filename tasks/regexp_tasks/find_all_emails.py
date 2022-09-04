"""
Написать функцию find_emails, которая принимает текст и находит в нем
все email вида some@some.some
"""
import re


def find_emails(email):
    return re.findall(r"\w+@[\w.]+", email)
