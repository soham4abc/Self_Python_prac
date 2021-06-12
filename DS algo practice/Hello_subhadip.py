def sum(a,b):
    k=int(a)+int(b)
    return k
def sub(c,d):
    l=int(c)-int(d)
    return l
def barbar(n,m):
    n=int(n)
    m=int(m)
    for i in range(n,m+1):
        print(i)


a1=input()
a2=input()
res=sum(a1,a2)
res1=sub(a1,a2)
barbar(a1,a2)
print("The result is : ",res1)
