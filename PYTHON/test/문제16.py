# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = input()
cnt = 0
for c in word:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        cnt += 1
print(cnt)