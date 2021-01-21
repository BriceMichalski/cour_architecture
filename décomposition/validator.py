import re

def is_present(a):
    return a is not None

def is_valid(value):
    return True if re.match(
        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9]*\.[a-z]{2,3}$",
        value
    ) else False

def is_spam(email,spam_list):
    return email.split("@")[1] in spam_list
