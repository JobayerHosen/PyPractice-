def count_substring(string, sub_string):
    counter = 0
    index = 0
    while string.find(sub_string, index) != -1:
        if string.find(sub_string, index) != -1:
            counter += 1
            index += string.find(sub_string, index) + 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)