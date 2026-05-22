li=[10,45,67,23,89,34]
n=len(li)
for i in range(n):
    for j in range(0,n-i-1):
        if(li[j]>li[j+1]):
            temp=li[j]
            li[j] = li[j+1] 
            li[j+1]=temp 
print('sorted list:',li)
print('second lagest number:',li[-2])            

