# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

# 1) while 문
n = 1
num = 1
while n <= 10:
    num *= n
    n += 1
print(num)

# 2) for 문
num = 1
for n in range(1,11):
    num *= n
    n += 1
print(num)