T = int(input())

for test_case in range(T):
    A, B = input().split()                      # 두 단어 A, B

    a = sorted(A)                               # A 알파벳 순서대로 정렬
    b = sorted(B)                               # B 알파벳 순서대로 정렬

    if a == b:                                  # 정렬한 두 단어가 같으면
        print(f'{A} & {B} are anagrams.')       # anagrams
    else:                                       # 다르면
        print(f'{A} & {B} are NOT anagrams.')   # NOT anagrams