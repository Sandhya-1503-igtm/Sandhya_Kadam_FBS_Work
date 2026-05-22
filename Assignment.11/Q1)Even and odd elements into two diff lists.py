li=[10,15,20,25,30,35]
even_li=[]
odd_li=[]
i=0
while(i<len(li)):
    if(i%2==0):
        even_li=even_li+[li[i]]
    else:
        odd_li=odd_li+[li[i]]
    i=i+1
print("Even List:",even_li)
print("Odd List:",odd_li)


           
           