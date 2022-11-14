import sys

sys.stdin = open("PYTHON/swea/2063_input.txt", "r")

N = int(input())  # N개의 숫자
middle = N // 2  # 중간값은 N//2번째

N_list = list(map(int, input().split()))  # 숫자 리스트
sorted(N_list)  # 오름차순 정렬

print(N_list[middle])  # N//2번째 값 출력
