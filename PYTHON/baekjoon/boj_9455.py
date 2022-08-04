T = int(input())

for test_case in range(T):
    m, n = map(int, input().split())

    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))

    move = 0
    for j in range(n):
        for i in range(m):
            if grid[i][j] == 1:
                for k in range(i+1, m):
                    if grid[k][j] == 0:
                        move += 1
                        
    print(move)