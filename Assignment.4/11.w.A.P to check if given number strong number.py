num=int(input('Enter number'))
temp=num
sum=0
while(temp>0):
    d=temp%10
    fact=1
    for i in range(1,d+1):
          fact=fact*i
          sum+=fact
          temp//10
          if(sum==num):
              print('Strong Number')
          else:
              ('Not strong')
                        

    
    

              

    
