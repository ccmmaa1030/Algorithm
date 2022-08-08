seven = []
for i in range(9):
    seven.append(int(input()))

for i in range(8):
    for j in range(i+1, 9):
        if sum(seven) - (seven[i] + seven[j]) == 100:
            no_1 = seven[i]
            no_2 = seven[j]

seven.remove(no_1)
seven.remove(no_2)

seven.sort()
for i in seven:
    print(i)