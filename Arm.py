def armstrong(a):
    num = a
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        k=isPalindrome(num)
        if (k!=num):
            print (num)



def isPalindrome(s):
        s=str(s)
        s1 =s[::-1]
        return s1
for i in range (100,1001):
    armstrong(i)