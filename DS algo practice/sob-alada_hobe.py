def alada(a):
    l=len(a)
    a1=""
    a2=""
    a3=""
    for i in range (0,l):
        if (a[i]==" "):
            a1+=a[i]

        elif (a[i] == 'A' or a[i] == 'a' or a[i] == 'E' or a[i] == 'e' or a[i] == 'I'
                or a[i] == 'i' or a[i] == 'O' or a[i] == 'o' or a[i] == 'U' or a[i] == 'u'):
            a2 +=a[i]
        else:
            a3+=a[i]

    a4=a2+a1+a3

    print (a4)
k=input()
alada(k)


