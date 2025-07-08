def count(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return len(result)
    return wrapper

# Getting males from the data
@count
def get_females(data):
  return [entry for entry in data if entry.Gender == '1']


# Getting femlaes from the data
@count
def get_males(data):
 return [entry for entry in data if entry.Gender == '2']