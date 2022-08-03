chess = []
for i in range(8):
    chess.append(list(input()))

white = 0
for i in range(8):
    for j in range(8):
        if chess[i][j] == 'F':
            if (i+j)%2 == 0:
                white += 1

print(white)