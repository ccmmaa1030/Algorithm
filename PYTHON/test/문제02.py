# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수 없이

word = 'happy!'
len = 0
for char in word:
    if char != '':
        len += 1
print(len)