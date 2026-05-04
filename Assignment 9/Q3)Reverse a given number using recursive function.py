def reverse(num,rev=0):
    if num==0:
        return rev
    else:
        d=num % 10
        rev=rev*10+d
        return reverse(num//10,rev)

num=int(input('Enter number'))
res=(reverse (num))


print("Reversed number is:", res)



    
    


      