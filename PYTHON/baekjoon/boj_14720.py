N = int(input())
milk_shop = list(map(int, input().split()))

drink = 0

for i in range(N):
    if milk_shop[i] == drink % 3:
        drink += 1

print(drink)