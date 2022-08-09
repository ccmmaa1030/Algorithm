import sys                              # 여러 줄 입력받기 위해 sys.stdin.read()
eng = sys.stdin.read()                  # 입력 종료할 때는 cntl+Z 누르고 enter

alphabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 종류
cnt = {}                                # 알파벳 개수 딕셔너리

for c in alphabet:                      # 알파벳 a~z까지 순서대로
    if c in eng:                        # 알파벳이 영어 문장 eng에 있으면
        cnt[c] = eng.count(c)           # 해당 알파벳을 key, 개수를 value로 추가

for key in cnt.keys():                  # cnt 딕셔너리의 key(알파벳) 순서대로
    if cnt[key] == max(cnt.values()):   # 해당 key의 값이 최대 알파벳 개수와 같으면
        print(key, end='')              # 해당 key를 연달아 출력