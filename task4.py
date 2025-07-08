from task2 import count, get_females, get_males
from collections import defaultdict, Counter

def drink_stats(data):
    
    dict = defaultdict(int)

    for entry in data:
        dict[entry.drink]+=1
            
    return dict

def exercise_stats(data, x):
    temp = [entry for entry in data if entry.exercise == x]
    return get_males(temp), get_females(temp)

# Students loving McDonald's fries
Mcdonalds_fries = count(lambda my_data:[entry for entry in my_data if entry.fries == '1'])

bright_students = lambda my_data: [entry for entry in my_data if entry.GPA > '3' and (entry.income =='5' or entry.income == '6')]

# Getting weight stats
def weight_stats(data, x):
    d=defaultdict(int)
    for entry in data:
        if entry.weight.isnumeric():
            d[entry.weight]+=1
    c = Counter(d)
     
    most = c.most_common(x)
    mweight_result = [i[0] for  i in most]

    least = c.most_common()[:-x-1:-1]
    lweight_result = [i[0] for  i in least]
    
    female = get_females([entry for entry in data if entry.weight in mweight_result])
    male = get_males([entry for entry in data if entry.weight in lweight_result])
    return female,male