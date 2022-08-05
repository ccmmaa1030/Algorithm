import sys
sys.stdin = open("PYTHON/swea/1218_input.txt", "r")

for test_case in range(1, 11):
    pair = {'()':0, '[]':0, '{}':0, '<>':0}
    length = int(input())
    word = input()
    possible = 1
 
    for c in word:
        for key, value in pair.items():
            if c in '([{<' and c in key:
                pair[key] += 1
            elif c in ')]}>' and c in key:
                pair[key] -= 1
         
    for key, value in pair.items():
        if value != 0:
            possible = 0
             
    print(f'#{test_case} {possible}')