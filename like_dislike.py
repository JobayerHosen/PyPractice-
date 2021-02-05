# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split(' ')
li = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
happiness = 0


#THIS SOLUTION IS NOT EFFICIENT
# notinA = (set(li) - A)
# happiness += n - len(notinA)
# for i in notinA:
#     happiness -= li.count(i) -1
# notinB = (set(li) - B)
# happiness -= (n - len(notinB))
# for i in notinB:
#     happiness += li.count(i) -1


for i in li:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)
