def gpa_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [entry for entry in result if entry.GPA.replace('.', '1').isnumeric()]
        return result
    return wrapper


def gender_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [entry for entry in result if entry.Gender == '1' or entry.Gender =='2']
        return result
    return wrapper


def drink_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [entry for entry in result if entry.drink == '1' or entry.drink =='2']
        return result
    return wrapper


def exercise_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        l = ['1', '2', '3', '4', '5']
        result = [entry for entry in result if entry.exercise in l]
        return result
    return wrapper


def fries_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [entry for entry in result if entry.fries == '1' or entry.fries =='2']
        return result
    return wrapper


def income_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        l = ['1', '2', '3', '4', '5', '6']
        result = [entry for entry in result if entry.income in l]
        return result
    return wrapper


def sports_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [entry for entry in result if entry.sports == '1' or entry.sports=='2']
        return result
    return wrapper


def weight_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [entry for entry in result if entry.weight.isnumeric()]
        return result
    return wrapper
