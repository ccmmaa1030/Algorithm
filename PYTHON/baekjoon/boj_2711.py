T = int(input())

for test_case in range(1, T+1):
    place, word  = input().split()
    place = int(place)

    word = word[:place-1] + word[place:]
    print(word)