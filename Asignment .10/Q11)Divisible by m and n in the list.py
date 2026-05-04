li=[10,15,6,20,12,30]
m=2
n=5
res=[]
for i in li:
    if(i%m==0 and i%n==0):
        res.append(i)
print('Divisible by  both:',res)        