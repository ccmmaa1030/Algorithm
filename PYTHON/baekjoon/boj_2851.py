score = 0
mushroom = []

for i in range(10):
    mushroom.append(int(input()))

for point in mushroom:
    score += point
    if score > 100:
        if score - 100 > 100 - (score - point):
            score = score - point
        break

print(score)