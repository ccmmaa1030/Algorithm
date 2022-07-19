# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = int(input())
result = 0

while True:
    result += number % 10
    number = number // 10
    if number == 0:
        break

print(result)