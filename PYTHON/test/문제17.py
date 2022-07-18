# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

word = input()
upper = ''
for c in word:
    upper += chr(ord(c)-32)
print(upper)