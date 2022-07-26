win_no = 0
win_score = 0

for i in range(1, 6):
    score = sum(list(map(int, input().split())))
    if score > win_score:
        win_score = score
        win_no = i
    
print(win_no, win_score)