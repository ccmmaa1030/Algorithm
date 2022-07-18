# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

for x in range(2, 10):
    a = f'{x}단'
    print(a)
    for y in range(1, 10):
        b = f'{x} X {y} = {x*y}'
        print(b)