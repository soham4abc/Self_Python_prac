def vowelcheck(st):
    st=st.upper()
    vowel=['A','E','I','O','U']
    l=len(st)
    for i in range(0,l):
        if(st[i] in vowel ):
            print(st[i],end="")
    print("\n")

print("enter number of names")
a=int(input())
for i in range (1,a+1):
    s=input()
    vowelcheck(s)

