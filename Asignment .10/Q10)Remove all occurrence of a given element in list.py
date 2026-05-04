li=[10,20,20,30,40,20]
n=int(input('Enter element to remove' ))
res=[]
for i in li:
    if (i!=n):
        res.append(i)
print(res)        