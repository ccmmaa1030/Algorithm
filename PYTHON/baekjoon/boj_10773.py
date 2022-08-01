K = int(input())
num = []

for i in range(K):
    N = int(input())
    if N == 0:
        num.pop()
    else:
        num.append(N)

result = sum(num)
print(result)