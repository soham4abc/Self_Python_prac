print("Enter the number of candles")
n=int(input())
ar=[]
print("EMA values of candle:")
for i in range (0,n):
    ar.append(int(input()))
for i in range (0,n-3):
    if (ar[i]>10):
        if((ar[i+1]>10) and(ar[i+2]>10)):
            print("Buy order passed!!")
            break;

