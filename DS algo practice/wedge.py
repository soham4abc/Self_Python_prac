a= int (input())
for i in range(1,a):
    for j in range(0,i):
        print("* ",end="")
    print("\n")
for i in reversed(range(1,a-1)):
    for j in range(0,i):
        print("* ",end="")
    print("\n")