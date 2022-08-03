T = int(input())
money_2017 = {500:1, 300:3, 200:6, 50:10, 30:15, 10:21}
money_2018 = {512:1, 256:3, 128:7, 64:15, 32:31}

for test_case in range(T):
    a, b = map(int, input().split())
    a_money = 0
    b_money = 0
    
    for key, value in money_2017.items():
        if a == 0:
            break
        elif a <= value:
            a_money = key
            break
    
    for key, value in money_2018.items():
        if b == 0:
            break     
        elif b <= value:
            b_money = key
            break

    result = (a_money + b_money) * 10000
    print(result)