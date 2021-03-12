def RevFind ():
    for i in range (100,1001):
        k1=str(i)
        s1=reverse(k1)
        if (s1==k1):
            print (s1)
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

RevFind()