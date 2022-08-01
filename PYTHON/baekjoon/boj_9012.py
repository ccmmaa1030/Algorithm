T = int(input())

for test_case in range(T):
    PS = list(input())
    sum = 0

    for i in PS:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")