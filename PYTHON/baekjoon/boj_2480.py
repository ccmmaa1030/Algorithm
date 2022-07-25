dice = list(map(int, input().split()))

if dice[0] == dice[1] and dice[1] == dice[2]:
    money = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[0] == dice[2]:
    money = 1000 + dice[0] * 100
elif dice[1] == dice[2]:
    money = 1000 + dice[1] * 100
else:
    money = max(dice) * 100

print(money)