n = int(input('type a number: '))
for i in range(1,n):
	if i == 1 or i == 2:
		print(i)
		continue
	for j in range(2,int(i/2+2)):
		if i%j  == 0:
			break
		
	else:
		print(i)

