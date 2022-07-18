# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

word = input()
re_word = ''

for char in word:
    re_word = char + re_word
word = re_word
print(word)