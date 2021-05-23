def isboring(a):
    a=str(a)
    a1=(list(a))
    count=int(0)
    for i in range (0,len(a1)):
        i1=i+1
        if (((i1%2)==0) and((int(a1[i])%2)==0)):
            count+=1
        elif (((i1%2)!=0) and((int(a1[i])%2)!=0)):
            count+=1
    if(count==len(a1)):
        return True



n=int(input())
n1=n+1
while(n>0):
    start,end=input().split(" ")
    end=int(end)
    start=int(start)
    cnt=int(0)
    for i in range(start,end+1):
        chk=isboring(i)
        if(chk==True):
            cnt+=1
    print("Test Case #",n1-n,": ",cnt)
    n-=1


