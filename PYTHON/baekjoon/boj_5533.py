N = int(input())
score = [0] * N

game = []
for i in range(N):
    game.append(list(map(int, input().split())))

for j in range(3):
    round = [game[i][j] for i in range(N)]
    for i in range(N):
        if round.count(round[i]) == 1:
            score[i] += round[i]

for i in range(N):
    print(score[i])