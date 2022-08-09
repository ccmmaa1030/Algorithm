while True:
    eng = input()               # 영어 문장 입력
    if eng == '#':              # #을 입력 받으면
        break                   # 반복문 탈출

    cnt = 0                     # 모음 개수
    for c in eng:               # 영어 문장에서
        if c in 'aeiouAEIOU':   # 각 문자가 모음에 해당하면
            cnt += 1            # 모음 개수 1 증가
    print(cnt)                  # 최종 모음 개수 출력