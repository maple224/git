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


   data = swap(1, 16, data)#根据需要计算的节点更改数据

dist = [0]*scale
path = [0]*scale
sett = [0]*scale

for i in range(scale):
    dist[i] = data[0][i]
    if dist[i] == 0:
        dist[i] = 9999
        path[i] = -1
sett[0] = 1  
#初始化各个表格

for i in range(scale):
    minpath = 9999
    index = 0 #用来找到目前未计算的节点中距离初始节点最近的节点
    flag = 0
    for j in range(scale):
        if sett[j] == 0:
            flag = 1
            if minpath > dist[j]:
                index = j
                minpath = dist[j]

    if flag == 0:
        break
    for k in range(scale): # 找到最近的节点后根据他更新他相邻的节点距初始节点的距离
        if dist[k] > dist[index] + data[index][k]:
            dist[k] = dist[index] + data[index][k]
            path[k] = index
    sett[index] = 1
print(dist[scale - 1])    

index_find = scale - 1
list_ans = [scale - 1]
while True:
    list_ans.append(path[index_find])
    index_find = path[index_find]
    if(index_find == 0):
        break
print(list_ans[::-1])
11