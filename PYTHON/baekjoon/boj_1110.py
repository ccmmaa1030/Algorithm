N = input()
cycle = 0

if int(N) < 10:
    num = [0, int(N)]
else:
    num = list(map(int, N))

while True:
    sum = num[0] + num[1]
    if sum < 10:
        num = [num[1], sum]
        cycle += 1
    else:
        sum_num = list(map(int, str(sum)))
        num = [num[1], sum_num[1]]
        cycle += 1

    if int(N) < 10:
        if '0' + str(N) == str(num[0]) + str(num[1]):
            break
    else:
        if str(N) == str(num[0]) + str(num[1]):
            break

print(cycle)