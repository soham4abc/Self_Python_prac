
def running():
    for i in range (100,1001):
        print (i)
        


def check(a):
    print(a)
    l1=isArmstrong(a)
    l=isNotPalindrome(a)
    if (l1 == True) and (l == True):
        print(a)

def isArmstrong(j):
    j1=0
    j1=j
    print (j)
    s=int(0)
    while (j>0):
        print (j)
        d=int (j % 10)
        print (d)
        s=s+pow(d,3)
        j=j/10
    if (s==j1):
        print ("true")
        return True

    else:
        return False
def isNotPalindrome(k):
    k1 = str(k)
    k2= k1[::-1]
    if (k1==k2):
        return False
    else:
        return True

running()




