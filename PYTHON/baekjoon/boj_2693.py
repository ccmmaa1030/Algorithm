T = int(input())

for test_case in range(T):
    array = list(map(int, input().split()))
    array.sort()
    print(array[7])
