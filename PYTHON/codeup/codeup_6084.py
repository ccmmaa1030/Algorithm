h, b, c, s = map(int, input().split())
MB = h*b*c*s/8/1024/1024
print(format(MB, ".1f") + ' MB')