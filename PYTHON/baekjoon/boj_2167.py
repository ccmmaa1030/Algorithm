N, M = map(int, input().split())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())

    result = 0
    for row in range(i-1, x):
        for column in range(j-1, y):
            result += array[row][column]
    
    print(result)