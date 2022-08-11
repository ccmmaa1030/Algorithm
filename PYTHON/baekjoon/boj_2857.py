agent = [input() for i in range(5)]             # 5명의 첩보원명 리스트 
no_FBI = 0                                      # FBI가 아닌 요원의 수

for name in agent:                              # 첩보원명 순서대로 확인
    if 'FBI' in name:                           # FBI가 이름에 들어가면
        print(agent.index(name)+1, end=' ')     # 해당 이름 인덱스+1 출력
    else:                                       # FBI가 이름에 안들어가면
        no_FBI += 1                             # FBI가 아닌 요원의 수 1 증가

if no_FBI == 5:                                 # 5명이 모두 FBI가 아니면
    print('HE GOT AWAY!')                       # HE GOT AWAY! 출력