def automorphic(n):
    sq = int(n * n)
    n=int(n)
    while (n > 0):
        if (int(n % 10) != int(sq % 10)):
            #print((n%10)," ",sq%10)
            return False
        n = int(n/10)
        sq =int(sq/10)

    return True

print("enter numbers")
ar=input().split(" ")
l=len(ar)
for i in range(0,l):
    k=automorphic(int(ar[i]))
    if(k==True):
        print(ar[i]," Is automorphic")
    else:
        print(ar[i], " not automorphic")
