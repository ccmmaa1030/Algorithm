N = int(input())                    # 자연수 N 입력

while True:
    find = 'Yes'                    # 찾는 값이 맞는지 확인 초기값 Yes

    for n in str(N):                # N을 문자형으로 바꾸어 한 자리씩 확인
        if n != '4' and n != '7':   # 자리수가 4와 7이 아니라면
            find = 'No'             # 찾는 값이 아님 No
            N -= 1                  # N을 1씩 줄여가면서 금민수인지 확인

    if find == 'Yes':               # 모든 자리를 확인해도 find가 Yes이면
        print(N)                    # 해당 수를 출력
        break                       # 반복문 종료