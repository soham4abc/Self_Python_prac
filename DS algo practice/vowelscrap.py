def vowelcheck(st):
    st=st.upper()
    vowel=['A','E','I','O','U']
    l=len(st)
    for i in range(0,l):
        if(st[i] in vowel ):
            print(st[i],end="")
    print("\n")


