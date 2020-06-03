from functools import *
# def findme(name):
    # return name[0] == 'J' or name[0] == 'j'
names = ['John', 'jane', 'adam', 'Jobayer']
# found = filter(findme, names)
found = filter(lambda x: x[0].lower() == "j", names)
print(list(found))

upper = list(map(lambda x: x.upper(), names))
string = ' '.join(map(str, upper))
print(string)

factorial = reduce(lambda a,b: a * b, range(1, 6))
print(factorial)

