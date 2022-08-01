long = list(input())
short = ''

short += long[0]
for i in range(len(long)):
    if long[i] == '-':
        short += long[i+1]

print(short)