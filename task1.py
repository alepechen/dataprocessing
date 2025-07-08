import csv 
from collections import namedtuple


def group_values_with_columns(orig_data, req_col, **kwargs):
    Student = namedtuple('Student', 'GPA Gender drink exercise fries income sports weight')
    columns_index=[orig_data[0].index(name) for name in req_col]
    if kwargs: # if limit is passed
        individuals = orig_data[1:kwargs['n']+1]
    else:
        individuals = orig_data[1:51]
    grouped_data=[]
    for el in individuals:
        val=[el[i] for i in columns_index]
        grouped_data.append(Student._make(val))
    return grouped_data


# Columns you'll deal with in this project
#required_columns = ['GPA', 'Gender', 'drink', 'exercise', 'fries', 'income', 'sports', 'weight']

# This is how your method will be called
#grouped_data = group_values_with_columns(data, required_columns, n=60)