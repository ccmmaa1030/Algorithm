X, Y = input().split()

sum_XY = str(int(X[::-1]) + int(Y[::-1]))  
Rev_sum = int(sum_XY[::-1]) 

print(Rev_sum)