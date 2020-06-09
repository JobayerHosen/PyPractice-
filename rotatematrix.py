m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in m:
    print(i)
print()

t = []
for i in range(len(m)):
    t.append([])

    #(1):
    # for j in range(len(m)-1, -1, -1):
    #     t[i].append(m[j][i])

    #(2):
    # for j in reversed(m):
    #     t[i].append(j[i])

    #(3):
    [t[i].append(j[i]) for j in m[::-1]]

for i in t:
    print(i)