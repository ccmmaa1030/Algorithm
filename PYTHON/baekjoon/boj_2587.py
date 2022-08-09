num = [int(input()) for i in range(5)]  # 5개의 자연수 입력
num.sort()                              # 오름차순 정렬

avg = sum(num) // 5                     # 평균 구하기
mid = num[2]                            # 중앙값(5개 중 3번째) 구하기

print(avg)                              # 평균 출력
print(mid)                              # 중앙값 출력

# 만약 n개의 숫자가 주어진다면?
# num = [int(input()) for i in range(n)]
# avg = sum(num) // n
# mid = num[n // 2]