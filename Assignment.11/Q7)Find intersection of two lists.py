li1=[10,20,30,40]
li2=[30,40,50,60]
result=[]
for i in range(len(li1)):
    for j in range(len(li2)):
        if li1[i]==li2[j]:
            result=result+[li1[i]]
print('Intersection of two lists:',result)            