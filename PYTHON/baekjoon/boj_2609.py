num1, num2 = map(int, input().split())

for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        divisor = i
        break

multiple = num1 * num2 // divisor

print(divisor)
print(multiple)