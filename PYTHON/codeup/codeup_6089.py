a, r, n = map(int, input().split())
num = a
for i in range(0, n-1):
    num *= r
print(num)