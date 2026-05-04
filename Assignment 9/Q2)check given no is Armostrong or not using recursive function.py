def armstrong(num,digits):
    if num==0:

      return 0
    
    d=num%10
    return(d ** digits + armstrong(num//10, digits) )

num=int(input('Enter Number'))
digits=len(str(num))
result=armstrong(num,digits)

if result == num:
   print("Armstrong Number")

else:
   print("Not Armstrong Number")   