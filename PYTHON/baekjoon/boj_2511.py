A_card = list(map(int, input().split()))
B_card = list(map(int, input().split()))

A_score = 0
B_score = 0
last_win = ''

for round in range(10):
    if A_card[round] > B_card[round]:
        A_score += 3
        last_win = 'A'
    elif A_card[round] < B_card[round]:
        B_score += 3
        last_win = 'B'
    else:
        A_score += 1
        B_score += 1

print(A_score, B_score)

if A_score > B_score:
    print('A')
elif A_score < B_score:
    print('B')
else:
    if last_win == 'A':
        print('A')
    elif last_win == 'B':
        print('B')
    else:
        print('D')
