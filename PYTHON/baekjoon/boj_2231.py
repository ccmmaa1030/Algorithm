N = input()

for num in range(int(N)+1):
    num_list = list(map(int, str(num)))

    de_num = num + sum(num_list)

    if de_num == int(N):
        print(num)
        break
    if num == int(N):
        print(0)