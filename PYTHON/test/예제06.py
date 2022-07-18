# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# -> 튜플형은 한번 저장되면 변경, 추가, 삭제가 불가하므로 append()를 할 수 없음
# -> answer를 튜플형 ()이 아닌 리스트 []로 저장해야 함

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)