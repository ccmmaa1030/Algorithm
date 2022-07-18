# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# -> input()은 문자형으로 입력받아짐
# -> sum() 함수는 숫자형을 계산하는 함수이므로 문자형에 사용할 수 없음
# -> int() 함수를 통해 형변환 필요

numbers = map(int, input().split())
print(sum(numbers))