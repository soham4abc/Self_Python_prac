def letssearch (a):
     l=len(a)
     c=int(0)
     k=""
     for j in range(0,l):

         if (k==a[j]):
            j+=1
         else:
             k = a[j]

             for i in range(0,l):

                 if(a[i] == k):
                     a.replace(k,'')
                     l=len(a)
                     c+=1
             if (c!=1):
                 print(k,"->",c)
             else:
                print(k,"-> occurs once!!")
             c=0

     c=0


n = input()
letssearch(n)





