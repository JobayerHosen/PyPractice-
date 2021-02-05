def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    kevin = 0
    stuart = 0
    slen = len(string)
    for i in range(slen):
        if string[i] in vowel:
            kevin += int(len(string) - i)
    stuart = int(slen * (slen + 1)/2 - kevin)

    if kevin > stuart:
        print('Kevin', kevin, sep=' ')
    elif stuart > kevin:
        print('Stuart', stuart, sep=' ')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)