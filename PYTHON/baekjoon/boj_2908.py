A, B = input().split()

re_A = A[::-1]
re_B = B[::-1]

if int(re_A) > int(re_B):
    print(re_A)
else:
    print(re_B)


