def merge_the_tools(string, k):
    # your code goes here
    for i in range(k, len(string)+1, k):
        # ss = string[i-k:i]
        ss = []
        for j in range(i-k, i):
            if string[j] not in ss:
                ss.append(string[j])

        print(''.join(ss))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    