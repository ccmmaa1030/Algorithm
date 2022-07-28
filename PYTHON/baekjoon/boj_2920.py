ascending = '1 2 3 4 5 6 7 8'
descending = '8 7 6 5 4 3 2 1'

num = input()

if ascending in num:
    print('ascending')
elif descending in num:
    print('descending')
else:
    print('mixed')