A, B = input().split()
re_A = ''
re_B = ''
answer = ''

for i in A:
    re_A = i + re_A
for j in B:
    re_B = j + re_B

if int(re_A) > int(re_B):
    answer = re_A
else:
    answer = re_B

print(answer)


