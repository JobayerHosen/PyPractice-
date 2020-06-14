fil = open('quotes.txt', 'r+')
lines = fil.readlines()
fil.close()
au = lines[1]
au = au[:3]
quotes = {}
qurrent_quote = ''
for line in lines:
    if line[1] == '.':
        line = line[3:]
    if line[2] == '.':
        line = line[4:]
    if line[:3] == au:
        line = line.replace(au,'--')

    if line[0:2] != '--':
        qurrent_quote += line
    else:
        quotes[qurrent_quote] = line
        qurrent_quote = ''
    
qu = open("quote.txt", "a")
for k, v in quotes.items():
    qu.write(k)
    qu.write(v)