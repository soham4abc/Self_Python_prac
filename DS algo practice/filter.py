import json

strJsonArray = "[{\"id\":\"1\",\"name\":\"Jack\"},{\"id\":\"3\",\"name\":\"John\"},{\"id\":\"2\",\"name\":\"Joe\"}]"

strJsonObject = "[{\"id\":\"3\",\"name\":\"John\"},{\"id\":\"3\",\"name\":\"John\"},{\"id\":\"4\",\"name\":\"Sumon\"}]"

#  A JSON array must be loaded using JsonArray:

k = json.loads(strJsonArray)
l = json.loads(strJsonObject)
lengthofArray1 = len(k)
lengthofArray2 = len(l)
#print (lengthofArray1)
#print (lengthofArray2)
ar=["dumy"]



for x in k:
    p = x['name']
    p1 =x['id']
    #print (p)
    count =int(0)
    for y in l:
        q = y['name']
        q1=y['id']
        e = (p == q)
        e1=(p1==q1)
        #print(e)
        if (e and e1 )== True:
            #print (q)
            count+=1
    print (" ID ",p1,p," occurs ",count)
    #stri=str("name :"+ p+" ID: "+p1)
    #ar[x]=stri

#print(ar)

