import sys
sys.stdin = open("PYTHON/swea/1204_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    n = int(input()) 
    
    grade = list(map(int, input().split()))  
    max_score = 0   
    
    for score in range(101): 
        if grade.count(score) >= grade.count(max_score):
            max_score = score
    
    print(f'#{n} {max_score}')  