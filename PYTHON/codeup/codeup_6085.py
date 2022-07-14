w, h, b = map(int, input().split())
MB = w*h*b/8/1024/1024
print(format(MB, ".2f") + ' MB')