ar1=input().split(" ")
ar2=input().split(" ")

l1=len(ar1)
l2=len(ar2)
fin=[]
print ("Enter user choice::")
ch=input().split(" ")
cl=len(ch)
for i in range(0,cl):
    if ch[i] in ar1 or ch[i] in ar2:
        fin.append(ch[i])

    else:
        print(ch[i], "not present in our stocks")
print(fin)
