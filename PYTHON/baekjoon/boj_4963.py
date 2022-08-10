while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    land_sea = [list(map(int, input().split())) for i in range(h)]

