# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

number = int(input())

n = 0
num = {}
while True:
    num[n] = number % 10
    number = number // 10
    n += 1
    if number == 0:
        break

i = 0
result = 0
while True:
    result = result + (num[i]*(10**(n-1)))
    i += 1
    n -= 1
    if n == 0:
        break

print(result)