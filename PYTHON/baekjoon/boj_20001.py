start = input()
debug = []
if start == '고무오리 디버깅 시작':
    while True:
        duck = input()

        if duck == '문제':
            debug.append(1)
        elif duck == '고무오리':
            if not debug:
                debug.append(1)
                debug.append(1)
            else:
                debug.pop()
        elif duck == '고무오리 디버깅 끝':
            break

    if not debug:
        print('고무오리야 사랑해')
    else:
        print('힝구')