# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# -> char == "a" 이후는 or로 단순 연결만 했기 때문에 비교가 아닌 True값으로 인식됨
# -> 제대로 조건문을 입력해서 or로 연결해야 함

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)