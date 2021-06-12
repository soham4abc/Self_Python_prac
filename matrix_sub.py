matrix1=[[],[],[]]
matrix2=[[],[],[]]
res=[[],[],[]]
print("enter 1st matrix row wise:")
for i in range(0,3):
    for j in range(0,3):
        matrix1[i].append(int(input()))
print("enter 2nd matrix row wise:")
for i in range(0,3):
    for j in range(0,3):
        matrix2[i].append(int(input()))




for i in range(0,3):
    for j in range(0,3):
        res[i].append(int(matrix1[i][j]) - int(matrix2[i][j]))
print(res)