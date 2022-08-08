word = input()
find = input()

word = word.replace(find, '*')
cnt = word.count('*')

print(cnt)