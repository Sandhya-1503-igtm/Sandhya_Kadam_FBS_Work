def fact(n):
    if(n==1):
        return 1
    else:
        return n * fact(n-1)      

def sos(n):
    if(n==0):
        return 0 
    else:
        return fact(n) + sos(n-1)
      
n=5
res=sos(n)
print('Sum of seris :', res )


