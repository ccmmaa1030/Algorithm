K = int(input())

for k in range(1, K+1):
    math = list(map(int, input().split()))
    math.pop(0)

    math.sort()
    max = math[-1]
    min = math[0]
    
    gap = 0
    for i in range(len(math)):
        if i+1 == len(math):
            break
        if math[i+1] - math[i] > gap:
            gap = math[i+1] - math[i]
    
    print(f'Class {k}')
    print(f'Max {max}, Min {min}, Largest gap {gap}')
