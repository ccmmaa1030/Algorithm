PC = int(input())           # 컴퓨터 개수 = 정점
connect = int(input())      # 서로 연결된 컴퓨터 쌍의 수 = 간선

network = [[] for i in range(PC+1)]

for i in range(connect):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)  

virus = 1
virus_cnt = 1
for i in network[virus]:
    if network[virus][i] == True:
        virus_cnt += 1                  # 1과 연결된 컴퓨터들도 순회 필요