T = int(input())

for test_case in range(T):
    word = list(input().split())
    
    for i in range(len(word)):
        print(word[i][::-1], end=' ')
    print()