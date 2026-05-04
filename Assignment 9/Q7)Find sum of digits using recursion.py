def sum_digits(num):
    if(num==0):
        return 0
    else:
        return (num%10) + sum_digits(num//10)
    
num=int(input('Enter number'))
result=sum_digits(num)
print('Sum of digits:',result)    
