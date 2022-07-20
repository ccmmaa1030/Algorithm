import sys
sys.stdin = open("PYTHON/swea/2047_input.txt", "r")

word = input()

for c in word:
    if ord(c) >= 97 :
        print(chr(ord(c)-32), end='')
    else:
        print(c, end='')

