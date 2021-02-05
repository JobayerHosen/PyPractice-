import textwrap

def wrap(string, max_width):
    s = list(string)
    for i in range(max_width, len(string) + int(len(string)//max_width) -1, max_width +1):
        s.insert(i,'\n')
    return ''.join(s)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)