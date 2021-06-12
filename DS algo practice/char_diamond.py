a=int(input())
hf=a//2
ch= str('A')

for i in range(0,a):
    ch='A'
    for j in reversed(range(i,hf+3)):
        print(end=" ")
    for j in range(1,(i+1)):
        print(ch,end=" ")
        ch=chr(int(ord(ch[0])+1))
    print(("\n"))

for i in reversed(range(0,a-1)):

    for j in reversed(range(i,hf+3)):
        print(end=" ")
    for j in range(1,(i+1)):
        print(ch,end=" ")
        ch=chr(int(ord(ch[0])+1))
    print(("\n"))
