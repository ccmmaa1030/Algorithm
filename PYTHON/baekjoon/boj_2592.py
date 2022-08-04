num = []
for i in range(10):
    num.append(int(input()))
avg = sum(num) // 10

num_set = list(set(num))
num_cnt = []
for j in num_set:
    num_cnt.append(num.count(j))
max_num = num_set[num_cnt.index(max(num_cnt))]

print(avg)
print(max_num)