arr = []
print("enter size of array")
n = int(input())
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
a1 = []
for i in reversed(range(0, n)):
    ele=arr[i]
    a1.append(ele)
for i in range(0, n):
    if((a1[i] % 2) == 0):
        print ("even")
    else:
        print ("Odd")



