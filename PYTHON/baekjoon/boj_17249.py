TaeBo = input()

TaeBo = TaeBo.split('(^0^)')
left = TaeBo[0].count('@')
right = TaeBo[1].count('@')

print(left, right)

