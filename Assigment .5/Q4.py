n=int(input('Enter number'))

for n in range(1,n+1):
    temp=n
    digits=len(str(n))
    s=0

    while temp>0:
        d=temp%10
        s+=d**digits
        temp//=10
    if(s==n):
        print(n)    