A_num, B_num = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_B = list(set(A) - set(B))
B_A = list(set(B) - set(A))
result = len(A_B) + len(B_A)

print(result)