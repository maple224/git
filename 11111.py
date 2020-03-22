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

for i in range(scale):
    for j in range(scale):
        if data[i][j] == 0:
            data[i][j] = 9999
#数据更改,9999代表不连通
            
def swap(m, n, data):
    data_swap = [[0]*scale for i in range(scale)]
    
    for i in range(scale):
        for j in range(scale):
            data_swap[i][j] = data[i][j]
            if i == m:
                data_swap[i][j] = data[n][j]
            elif i == n:
                data_swap[i][j] = data[m][j]
            if j == m:
                data_swap[i][j] = data[i][n]
            elif j == n:
                data_swap[i][j] = data[i][m]
    return data_swap
