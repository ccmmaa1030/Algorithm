# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]
max = 0
max2 = 0
for i in numbers:
    if max < i:
        max2 = max
        max = i
    else:
        max2 = i
print(max2)