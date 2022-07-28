num = []

for i in range(10):
    num.append(int(input())%42)

count = len(set(num))
print(count)