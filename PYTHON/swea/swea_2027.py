import sys
sys.stdin = open("PYTHON/swea/2027_input.txt", "r")

for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print('#', end='')
        else:
            print('+', end='')
    print()