for n in range(2, 50):

    for x in range(2, n):
        if n % x == 0:
            print(n, "is not prime", sep=' ')
            break

    else:
        print(n, "is prime", sep=' ')   #for...else | else block runs if no 'break' occurs in the for loop. similar to try...else.