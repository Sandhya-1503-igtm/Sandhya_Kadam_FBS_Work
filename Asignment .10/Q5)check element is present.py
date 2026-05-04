li=[10,20,30,40,50,40,10]
n=int(input('Enter number'))
count=0
for i in li:
    if(i==n):
        count+=1
if count > 0:
    print("Present",count,"times")
else:
    print("Not Present")            
