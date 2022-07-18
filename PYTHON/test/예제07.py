# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# -> 총 개수 count를 구하기 위해서는 count += 1 코드가 for문 안에 들어가야 함
# -> // 연산자는 정수 부분의 몫만 출력되므로 / 연산자를 사용해야 함

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)