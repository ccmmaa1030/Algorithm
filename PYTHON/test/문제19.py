# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

number = int(input())
n = 0
cnt = {}
if number > 0:
    while True:
        cnt[n] = number % 10
        number = number // 10
        n += 1
        if number == 0:
            break
    count = len(cnt)
else:
    count = 1

print(count)