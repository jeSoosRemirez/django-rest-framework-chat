import re

REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def email_validator(email):
    if re.search(REGEX, email):
        return True
    return False


def text_validator(text):
    if len(text) <= 100:
        return True
    return False
