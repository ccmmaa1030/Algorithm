A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
cnt = [0] * 10

for i in range(len(cnt)):
    for num in result:
        if int(num) == i: 
            cnt[i] += 1
    print(cnt[i])