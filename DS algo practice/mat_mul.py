res = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

def multiply(a,b):
    for i in range (0,3):
        for j in range(0,3):
            for k in range(0,3):
                res[i][j]+=a[i][j]*b[k][j]
    for r in res:
        print(r)

a1=[]
b1=[]
print("enter 1st array row wise")
for i in range(0,3):
    a =[]
    for j in range(0,3):
         a.append(int(input()))
    a1.append(a)

print("enter 2nd array row wise")
for i in range(0,3):
    a =[]
    for j in range(0,3):
         a.append(int(input()))
    b1.append(a)

multiply(a1,b1)


