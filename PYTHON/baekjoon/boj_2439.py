N = int(input())

for i in range(1, N+1):
    gap = N-i
    star = ' ' * gap + '*' * i
    print(star)