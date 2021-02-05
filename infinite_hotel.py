#NOT EFFICIENT
# k, tourists = int(input()), list(map(int, input().split(' ')))
# ans = int(( (sum(set(tourists)) * k) - sum(tourists) ) / (k - 1) )
# print(ans)

A = set()
B = set()
k= int(input())
for i in input().split(' '):
    if i not in A:
        A.add(i)
    else:
        B.add(i)
print(*A-B)
