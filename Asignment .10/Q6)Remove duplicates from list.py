li=[1,2,3,3,5,6,2]
unique=[]
for i in li:
    found=0
    for j in unique:
            if i==j:
                  found=1
                  break
    if found==0:
        unique.append(i)
print('Afetr removing duplicates:',unique)