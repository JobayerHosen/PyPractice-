# a = set('Jobayer')
# b = set('Hosen')
# c = a ^ b
# d = (a | b) - (a & b)
# print(d == c)

a = 'jobayer'
d = {x : x.upper() for x in a}

for k, v in d.items():
    print(k,v,sep=':')

