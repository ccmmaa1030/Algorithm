T = int(input())

for test_case in range(T):
    s = int(input())
    n = int(input())
    
    for option in range(n):
        q, p = map(int, input().split())
        s += q * p
    
    print(s)