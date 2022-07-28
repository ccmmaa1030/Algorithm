delete = 'CAMBRIDGE'
word = input()

for c in word:
    if c in delete:
        word = word.replace(c, '')

print(word)