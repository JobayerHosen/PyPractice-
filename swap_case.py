def swap_case(s):
    r = ''
    for c in s:
        if ord(c) >= 65 and ord(c) <= (65+25):
            c = chr(ord(c) + 32)
        elif ord(c) >= 97 and ord(c) <= (97+25):
            c = chr(ord(c) - 32)
        else:
            pass
        r += c
    return r
if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)