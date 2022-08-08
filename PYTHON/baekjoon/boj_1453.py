N = int(input())
man = list(map(int, input().split()))
pc = []
no = 0

for i in man:
    if i not in pc:
        pc.append(i)
    else:
        no += 1

print(no)