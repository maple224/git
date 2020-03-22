global scale
scale = 17
data = [[0]*scale for i in range(scale)]
"""
for i in range(scale):
    data[i]= list(map(int, input().split()))
"""
#第二题初始化

data = [[0]*scale for i in range(scale)]
m, n = 0, 0

for i in range(13):
    list_temp = list(map(int, input().split()))
    for j in range(len(list_temp)):
        if(list_temp[j] != 0):
            data[m][n] = list_temp[j]
            data[n][m] = data[m][n]
            m += 1
        else:
            m = 0
            n += 1
#第一题初始化